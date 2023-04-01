
import matplotlib.pyplot as plt 
import numpy as np
from scipy.linalg import hilbert

def func(ndim, x,A,b):   #J(x)= 1/2 *(Ax,x) - (b,x)
    f = 0.5*(A.dot(x)).dot(x)-b.dot(x)
    return f
    

def gradFunc(ndim, x,A,b):   # le victeur gradient de la fonction f
    fp = A.dot(x)-b
    return fp

def CalcuGradia(ndim,pas,x,choix,A,b):# cette fonction calcule le gradian d'une fonction par la méthode de différence fini
    if choix == 0:
        dfdx = gradFunc(ndim, x,A,b)
    elif choix ==1 :
        dfdx = []
        for i in range(0, ndim):
            x[i]=x[i]+ pas            # x_i + h avec h = pas
            fp = func(ndim, x,A,b)          # f(x_i+h)) 
            x[i]=x[i]- 2*pas           # x_i - h 
            fm = func(ndim, x,A,b)          # f(x_i - h)
            dfdx.append((fp-fm)/(2*pas))
    norm_grad = Ps(ndim, dfdx, dfdx)
    return dfdx,norm_grad

        
def Ps(ndim, v1, v2):   
    ps = 0
    for i in range(ndim):
        ps += v1[i]*v2[i]
    return ps
        
def MethGradian(ndim,choix,ro0,dfdx,x,A): 
    xmax=np.ones((ndim))*200     # bornne sup du vecteur x
    xmin=-np.ones((ndim))*200    # bornne inf du vecteur x 
    
    if choix==0:    # gradiant simple
        d = - ro0*np.array(dfdx)
            
    if choix ==1:               # descente (see conjugate gradient polack-ribiere 2.7.9 poly)
        d = dfdx
        ro = Ps(ndim, d, d)/ (Ps(ndim, A.dot(d), d))
        d = - ro*np.array(d)

    for i in range(0, ndim):
        x[i]= x[i] + d[i]              #xn+1=xn+rho * d (= -gradj)
        x[i]=max(min(x[i], xmax[i]), xmin[i])   #Box constraint
    return x


ndim = 10
ro0  = 0.01
x=np.ones((ndim))         


choix2 = 1 # choix de la methode pour aprocher x : 1 ==> Gradiant conjugué // 0 ==>Gradiant simple
choix1 = 0 # choix de la methode de calcule de gradiant : 1 ==> differance fini // 0==> Gradiant direct
NbIter = 100 # minim iterations
pas=0.001  #FD step to approx grad


# declaration des variables A, b, x0, ro0 (si on travail sur G.S).
A= hilbert(ndim)
xcible=list(range(0, ndim))
b= A.dot(xcible)

ro0=0.1
historyg =[]
history  = []

"""
def main():
    print("ce code est pour la resolution des equations Ax = b ")
    ndim = int(input("insert la dimention de la vecteur x :  ") )
    A = input("insert la matrice A :  ")
    b = input("insert la matrice b ")
    x = input("insert x0 : ")
    ro0 = float(0.01)
    choix2 = int(input("choisi 1 pour la difference fini et 0 pour Gradiant exacte "))
    if choix2 == 1:
        pas =float(input("insert le pas : "))
    else:
        pass
    choix1 = int(input("choisi 1 pour Gradiant conjugué et 0 pour Gradiant simple "))
    if choix2 == 0:
        pas =float(input("insert le ro 0 : "))
    else:
        pass
    NbIter = int(input("insert le Nb des iterartion minimale : "))
    
"""
for itera in range(NbIter): # main code 
        dfdx,res = CalcuGradia(ndim, pas, x, choix1,A,b)
        historyg.append(res)
        historyg[itera] = historyg[itera]/abs(historyg[0])
        x  = MethGradian(ndim, choix2 , ro0,dfdx, x,A)
        f = func(ndim, x, A, b)
        history.append(f)
        if res < 1.e-30 :
            break
# gradiant behaviors
if choix2==1:  
    plt.plot(historyg, color='red', label='GD')
    plt.xlabel('Iteration')
    plt.ylabel('||∇J(x)||')
    plt.title('Gradiant conjugué')
if choix2==0:
    plt.plot(historyg, color='green',label='CG')
    plt.xlabel('Iteration')
    plt.ylabel('||∇J(x)||')
    plt.title('Gradiant simple')

#Fonctionnelle behaviors
plt.figure()
plt.plot(history)
plt.xlabel('Iteration')
plt.ylabel('J(x)')
plt.title('Fonctionnelle')
        
Ainv = np.linalg.inv(A)
xexcate = np.dot(Ainv,b)

print(" la valeur approcher :", x)
print(" la valeur exacte :", xexcate)

print("le nombre d'iteration est :",itera, "|∇J(x)|| finale = :", res) # nombre iteration minimale 

# comparaison graphique de solution exacte avec solution approcher
plt.figure()   
plt.annotate('solution exacte', xy=(1, xexcate[1]),arrowprops=dict(facecolor='green'))
plt.annotate('solustion approché', xy=(ndim-1, x[ndim-1]),arrowprops=dict(facecolor='blue'))
plt.plot(xexcate, color='green')  
plt.plot(x, color='blue')
plt.title("comparaison de la solution")
# %%
