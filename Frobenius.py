#Programe un algoritmo para encontrar 
# la norma de Frobenius para una matriz cuadrada 
# de cualquier dimensión.

import numpy as np
# ingreso el numero de filas y columnas debe ser matriz cuadrada
filas = int (input('Digite la cantidad de Filas: '))
columnas = int (input('Digite la cantidad de columnas: '))
matriz =[]
for i in range(filas): #ingreso de valores para fila y columna
    matriz.append([])
    for j in range(columnas):
        valor=float(input("Fila{}, Columna{}: ".format(i+1, j+1)))
        matriz[i].append(valor)


print('La  Matriz que ingreso es la siguiente:')
print()
for fila in matriz:
    print("[" , end="")
    for elemento in fila:
        print("{:8.2f}".format(elemento), end="")
    print("]")
print()

#calculo de la norma de Frobenius
norma=np.linalg.norm(matriz, 'fro')
#Muestro el valor de la Norma
print('La norma de Frobenius es: ')
print(norma)

#condicion=np.linalg.cond(matriz, 'fro')
#print('La condicon de Frobenius es: ')
#4print(condicion)