import numpy as np #usage de matrice #
import collections as cl #permet de donner les occurences des modalités dans une variable #
import pandas as pd #permet de charger les données #
import math #usage des fonctions mathématiques #

data = pd.read_csv('C:\\Users\\SCD UM\\Desktop\\AD\\logtsDK (5).csv',sep = '\t')
A=(np.mean(data.iloc[:,1:12]))
B=(np.std(data.iloc[:,1:12]))
C=data.iloc[:,1:12]-A
Cm=np.matrix(C) #matrice centréé#
D=data.iloc[:,1:12] 
Dm=np.matrix(D)
def poids(S): #vecteur poids #
    
        j=np.zeros(11) 
        j=sum(S)
                #Permet de retrouver la somme globale des 11 variables#
        x=0
        for i in range(0,11):
            x=x+j[:,i] 
        j=int(x) ; poids=np.zeros(41)
        for u in range(0,41):
            e=int(np.sum(S[u:(u+1),:]))
            poids[u]=e/j
        return poids

W=np.zeros((41,41))  #matrice diagonales des poids#
a=poids(Dm)
for i in range(0,41):
    for j in range(0,41):
        if (i==j):
            W[i,j]=a[i] # W: c'est la matrice diagonale des poids #

for i in range(0,11):
    Z=np.transpose(Cm[:,i])
    p=Z*W*Cm[:,i]
    Cm[:,i]=Cm[:,i]/(math.sqrt(p)) #martices centrés réduits#
#le barycentre du centre de gravité#
Gmoyenne=np.zeros(11)
for i in range(0,11):
    z=np.mean(Cm[:,i])
    if (abs(z) < 1.e-15):
        z=0
    Gmoyenne[i]=z
print('le barycentre est ',+Gmoyenne)
#inertie Total noté p#
p=0;
G=np.zeros(11) # a :c'est le vecteur des poids#
for i in range (0,41):
    l=Cm[i,:]
    dist=np.linalg.norm(l)**2
    p=p+dist*a[i]
print('l"inertie total du nuage   est ',+p)

#poids des modalités popu,bourge,moyen#
gc=data['StandingQuartier'].value_counts()#**#
pd=gc[0]/41
print('le poids pour popu est ',+pd)
pd=gc[1]/41
print('le poids pour  bourge est ',+pd)
pd=gc[2]/41
print('le poids pour moyen est ',+pd)

#barycentre des modalités#
Stand=(data.iloc[:,26:27])
ST=np.matrix(Stand)
moypop=moybour=moyen=0
pd1=gc[0]/41 ;pd2=gc[1]/41 ;pd3=gc[2]
for i in range(0,41):
    if (ST[i,:]=='popu'):
        moypop=moypop+(a[i]/pd1)*(i+1)
    if (ST[i,:]=='bourge'):
        moybour=moybour+(a[i]/pd2)*(i+1)
    if (ST[i,:]=='moy'):
        moyen=moyen+(a[i]/pd3)*(i+1)
print('le barycentre de la modalité popu est:',+moypop)
print('le barycentre de la modalité bourge est:',+moybour)
print('le barycentre de la modalité moyen est:',+moyen)

#Norme des modalités#
norm1=np.linalg.norm(moypop)**2
norm2=np.linalg.norm(moybour)**2
norm3=np.linalg.norm(moyen)**2
print('la norme carrée de popu est :',+norm1)
print('la norme carrée de bourge est :',+norm2)
print('la norme carrée de moy est :',+norm3)

#inertie externe puis on déduis l'inertie interne #
Iexterne=pd1*norm1+pd2*norm2+pd3*norm3
Iex=Iexterne/41
print('l"inertie externe  est :' ,+Iex)
Iinterne=11-Iex
print('l"inertie interne   est :' ,+Iinterne)
R2=Iinterne/11
print('la partition R2 est:',+R2)
data.plot()
