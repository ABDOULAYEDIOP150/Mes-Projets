# Question 1

CockVarQuant =as.matrix(cocktails[,3:15])
CockVarNom = as.matrix(cocktails[,1:2])


l<-colMeans(CockVarQuant) # moyenne de chaque colonne de la matrice #
vecmoy<-c(l)
Matmoy=matrix(0,189,13)
for (i in 1:13){
  Matmoy[,i]=vecmoy[i]
}
X=matrix(0,189,13)
#-------------------Centré La matrice X-----------------------#
for (i in 1:189){
  for (j in 1:13)
  {
    X[i,j]=CockVarQuant[i,j]-Matmoy[i,j]
  }
}
#------------------Réduire la matrice X------------------------#
W=1/189*diag(1,189,189)
for (i in 1:13){
  Z=t(X[,i])
  p=Z%*%W%*%X[,i]
  X[,i]=X[,i]/sqrt(p)
}


M=1/13*diag(1,13,13)
library("ade4")
CockVarNomIndic = as.matrix(acm.disjonctif(CockVarNom))
Y<-CockVarNomIndic[,1:12] 
Z<- CockVarNomIndic[,13:28]
library("matrixcalc")

#--------------------QUESTION 2----------------------------------#


ProjY<-(Y)%*%solve((t(Y)%*%W%*%Y))%*%t(Y)%*%W # Projection de Y#
ProjZ<-(Z)%*%solve((t(Z)%*%W%*%Z))%*%t(Z)%*%W # Projection de Z#

#-----------Projection de chaque individus X^j et trace associèe-------------------#

ProjX1=(X[,1])%*%solve((t(X[,1])%*%W%*%X[,1]))%*%t(X[,1])%*%W
traX1Y<-matrix.trace(ProjX1%*%ProjY)

ProjX2=(X[,2])%*%solve((t(X[,2])%*%W%*%X[,2]))%*%t(X[,2])%*%W
traX2Y<-matrix.trace(ProjX2%*%ProjY)

ProjX3=(X[,3])%*%solve((t(X[,3])%*%W%*%X[,3]))%*%t(X[,3])%*%W
traX3Y<-matrix.trace(ProjX3%*%ProjY)

ProjX4=(X[,4])%*%solve((t(X[,4])%*%W%*%X[,4]))%*%t(X[,4])%*%W
traX4Y<-matrix.trace(ProjX1%*%ProjY)

ProjX5=(X[,5])%*%solve((t(X[,5])%*%W%*%X[,5]))%*%t(X[,5])%*%W
traX5Y<-matrix.trace(ProjX1%*%ProjY)

ProjX5=(X[,1])%*%solve((t(X[,1])%*%W%*%X[,1]))%*%t(X[,1])%*%W
traX5Y<-matrix.trace(ProjX5%*%ProjY)

ProjX6=(X[,6])%*%solve((t(X[,6])%*%W%*%X[,6]))%*%t(X[,6])%*%W
traX6Y<-matrix.trace(ProjX6%*%ProjY)

ProjX7=(X[,7])%*%solve((t(X[,7])%*%W%*%X[,7]))%*%t(X[,7])%*%W
traX7Y<-matrix.trace(ProjX7%*%ProjY)

ProjX8=(X[,8])%*%solve((t(X[,8])%*%W%*%X[,8]))%*%t(X[,8])%*%W
traX8Y<-matrix.trace(ProjX8%*%ProjY)

ProjX9=(X[,9])%*%solve((t(X[,9])%*%W%*%X[,9]))%*%t(X[,9])%*%W
traX9Y<-matrix.trace(ProjX9%*%ProjY)

ProjX10=(X[,10])%*%solve((t(X[,10])%*%W%*%X[,10]))%*%t(X[,10])%*%W
traX10Y<-matrix.trace(ProjX10%*%ProjY)

ProjX11=(X[,11])%*%solve((t(X[,11])%*%W%*%X[,11]))%*%t(X[,11])%*%W
traX11Y<-matrix.trace(ProjX11%*%ProjY)

ProjX12=(X[,12])%*%solve((t(X[,12])%*%W%*%X[,12]))%*%t(X[,12])%*%W
traX12Y<-matrix.trace(ProjX12%*%ProjY)

ProjX13=(X[,13])%*%solve((t(X[,13])%*%W%*%X[,13]))%*%t(X[,13])%*%W
traX13Y<-matrix.trace(ProjX13%*%ProjY)

VectraceXJ<-c(traX1Y,traX2Y,traX3Y,traX4Y,traX5Y,traX6Y,traX7Y,traX8Y,traX9Y,traX10Y,traX11Y,traX12Y,traX13Y)
for (j in 1:13){
  print(VectraceXJ[j])
}

#----------------------trace de RProjY-----------------------------#

R=X%*%M%*%t(X)%*%W
traRProjY<-matrix.trace(R%*%ProjY)

#--------------------trace de ProjX^jProjZ-------------------------#


traProjX1ProjZ<-matrix.trace(ProjX1%*%ProjZ)

traProjX2ProjZ<-matrix.trace(ProjX2%*%ProjZ)

traProjX3ProjZ<-matrix.trace(ProjX3%*%ProjZ)

traProjX4ProjZ<-matrix.trace(ProjX4%*%ProjZ)

traProjX5ProjZ<-matrix.trace(ProjX5%*%ProjZ)

traProjX6ProjZ<-matrix.trace(ProjX6%*%ProjZ)

traProjX7ProjZ<-matrix.trace(ProjX7%*%ProjZ)

traProjX8ProjZ<-matrix.trace(ProjX8%*%ProjZ)

traProjX9ProjZ<-matrix.trace(ProjX9%*%ProjZ)

traProjX10ProjZ<-matrix.trace(ProjX10%*%ProjZ)

traProjX11ProjZ<-matrix.trace(ProjX11%*%ProjZ)

traProjX12ProjZ<-matrix.trace(ProjX12%*%ProjZ)

traProjX13ProjZ<-matrix.trace(ProjX13%*%ProjZ)

VectraceXJProjZ<-c(traProjX1ProjZ,traProjX2ProjZ,traProjX3ProjZ,traProjX4ProjZ,traProjX5ProjZ,traProjX6ProjZ,traProjX7ProjZ,traProjX8ProjZ,traProjX9ProjZ,traProjX10ProjZ,traProjX11ProjZ,traProjX12ProjZ,traProjX13ProjZ)
for (j in 1:13){
  print(VectraceXJ[j])
}


#----------------------------trace de RProjZ---------------------------------#

traRProjZ<-matrix.trace(R%*%ProjZ)

