
#Importo Librerias 
import numpy as np
import scipy
import scipy.linalg   
#Ingreso matriz
B = np.array([[4, 6, 10], [ 6, 3, 19], [10, 19, 62]])
print ("La matriz a apliacar el metodo de Cholesky es :")
print(B)
#Determino si la matriz es simetrica
def symmetrical(A):
    for i in range(0, 3):
        for j in range(0,3):
            if (B[i][j] != B[j][i]):
                print('La matriz es simetrica ')
                return False
            else:
                print('La matriz no simetrica ')
                return True
# Encuentre los valores propios de A 
D = np.linalg.eigvals (B) 
#determino si todos los valores propios son mayores que 0
if np.all (D> 0): 
    print( 'La matriz es definida Positiva ')
else:
    print('La matriz no es definida poritiva ')

# Una vez definida la matriz 
#Calculo de Matrices L y L^T
L = scipy.linalg.cholesky(B, lower=True)
LT = scipy.linalg.cholesky(B, lower=False)
#Muestro las matrices obtenidas
print ("La matrix L es :")
print(L)
print ("La matriz L^T es: ")
print(LT)

