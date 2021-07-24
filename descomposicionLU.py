
#Descomposicion LU
import numpy as np

# Ingreso de datos 
m=int(input("ingrese el numero de Filas: "))
matriz=np.zeros([m,m])
u=np.zeros([m,m])
l=np.zeros([m,m])
print("Ingrese los elementos de la matriz")
for f in range(0,m):
    for c in range(0,m):
        matriz[f,c]=(input("elemento a["+ str(f+1)+","+str(c+1)+"]"))
        matriz[f,c]=float(matriz[f,c])
        u[f,c]=matriz[f,c]

#para hacer ceros debajo de la diagonal principal
for k in range (0,m):
    for f in range(0,m):
        if (k==f):
            l[k,f]=1
        if(k<f):
            factor=(matriz[f,k]/matriz[k,k])
            l[f,k]=factor
            for c in range(0,m,1):
                matriz[f,c]=matriz[f,c]-(factor*matriz[k,c])
                u[f,c]=matriz[f,c]    
print('Descomposicion LU')
print('La Matriz l es:')
print(l)
print('Matriz U es:')
print(u)


