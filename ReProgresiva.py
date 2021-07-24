
#regresion Progresiva
import numpy as np #importo librerias

#ingreso las matrices 
A = np.array([[6, 0, 0, 0],
              [3, 6, 0, 0],
              [4, -2, 7, 0],
              [5, -3, 9, 21]])
B = np.array([12,-12, 14, -2])

n=4 #establesco una matriz cuadrada 
x=np.zeros([n])  # inicializio la variables con ceros
x[0]=B[0]/A[0,0]
#realizo las operaciones correspondientes 
# para la regresion progresiva 
for i in range(1,n,1): 
    ResultadoAx=0
    for j in range (0,i,1):
        ResultadoAx=ResultadoAx+A[i,j]*x[j]

    x[i]=(B[i]-ResultadoAx)/A[i,i]

XP=np.array(x).T #coloco los valores de X en forma de vector
print('Los valores de X con regresion progresiva son:')
print(' x1  x2  x3  X4')
print(XP)


