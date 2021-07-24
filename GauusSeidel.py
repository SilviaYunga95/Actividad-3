# importo libreria
import numpy as np
#ingreso matrices
A=np.array([[7,1,-1, 2],
        [1,8,0,-2],
        [-1,0,4,-1],
        [2,-2,-1,6]])
B=np.array([3,-5,4,-3])
n=A.shape[1]
#valor de K
k=7
kmax=100
#Calculo de Matrices para aplicar formulas 
D=np.eye(n)
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]
LU=D-A
L=np.tril(LU)
U=np.triu(LU)
G=D-L
Ginv=np.linalg.inv(G)
print('La matriz ingresada es:')
print(A)
#Ingreso datos necesarios para aplicar metodo de Jacobi
X=np.zeros(n)
Xant=np.copy(X)
xfin = ([1,-1,1,-1])
e = np.zeros(4)
tol=0.001;   
print('Los resultados utilizando el metodo de Jacobi son')
print('Iteracion   x1     x2       x3     x4')
#Calculo de iteracione 
for i in range(k):
        Ginv=np.linalg.inv(G)
        Xant=X
        X=np.dot(np.dot(Ginv,U),X)+np.dot(Ginv,B)
        print("      ",i+1, X.round(decimals=4))
#Calculo de error relativo para cada iteracion
print('Iteracion   er1     er2       er3     er4')
for i in range(k): 
        error=np.linalg.norm((X-Xant)/X)
        print('Iteracion',i+1,': error ',error.round(decimals=4))       
#Calculo del error relativo de la ultima iteracion con el valor 
# real de x propuesto en ele ejercicio
for i in range(4):
    e[i] = (xfin[i]-X[i])/xfin[i]
    print('El error final de x',i+1,'es:',abs(e[i]).round(decimals=4))

print('Iteracion  er1    er2     er3   er4')
print('       1 0.0 0.0 0.0 0.0')
print('       2 0.5125 0.2509 1.6470 0.2029')
print('       3 0.0942 0.0721 0.0356 0.0612')
print('       4 0.0221 0.0179 0.0094 0.0148')
print('       5 0.0054 0.0044 0.0022 0.0037')
print('       6 0.0014 0.0010 0.0005 0.0009')
print('       7 0.0003 0.0003 0.0002 0.0002')







