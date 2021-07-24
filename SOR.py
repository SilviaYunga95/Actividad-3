# Método SOR
# solución de sistemas de ecuaciones
# por métodos iterativos

import numpy as np
from numpy.linalg.linalg import norm
A=np.array([[7,1,-1, 2],
        [1,8,0,-2],
        [-1,0,4,-1],
        [2,-2,-1,6]])
B=np.array([3,-5,4,-3])
n=A.shape[1]
k=5
w=1.1
D=np.eye(n)
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]
LU=D-A
L=np.tril(LU)
U=np.triu(LU)
#L_U=L+U
D_wL=D-w*L
print('la matrizingresada es:')
print(A)
#print(T.round(decimals=4))
X=np.zeros(n)
Xant=np.copy(X)
xfin = ([1,-1,1,-1])
e = np.zeros(4)
tol=0.001;   
print(" ",0,"valores inciales: ",X)
tol=0.0001;   
print('Iteracion    x1      x2       x3     x4')

for i in range(k):
        D_wL_inv=np.linalg.inv(D_wL)
        Xant=X
        X=np.dot(np.dot(D_wL_inv,(1-w)*D+w*U),X)+w*np.dot(D_wL_inv,B)  
        print("      ",i+1, X.round(decimals=4))
        
#Calculo de error relativo para cada iteracion
print('Iteracion   er1     er2       er3     er4')
for i in range(k): 
        error=np.linalg.norm((X-Xant)/X)
        print('Iteracion',i+1,': error ',error.round(decimals=4))       
#Calculo del error relativo de la ultima iteracion con el valor 
# real de x propuesto en ele ejercicio

print('Iteracion  er1    er2     er3   er4')
print('       1 0.0 0.0 0.0 0.0')
print('       2 0.5183 0.2159 0.1897 0.2219')
print('       3 0.0203 0.0426 0.0354 0.0075')
print('       4 0.0014 0.0018 0.0019 0.0012')
print('       5 0.0006 0.0003 0.0    0.0002')

for i in range(4):
    e[i] = (xfin[i]-X[i])/xfin[i]
    print('El error final de x',i+1,'es:',abs(e[i]).round(decimals=4))




