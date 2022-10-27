
import numpy as np


def determinante(matriz):
    determinante = np.linalg.det(matriz)
    return determinante

matriz = np.array([[3,5,6,7,8],[1,2,3,4,5],[3,6,8,3,9],[8,3,8,5,1],[7,6,5,4,3]])
print(determinante(matriz))

def det(matriz):
    det=1
    for x in range(matriz):
        det= matriz[x][x]*det
    print('el determinante de la matriz es: ', det)

matriz1= [[3,5,6,7,8],[1,2,3,4,5],[3,6,8,3,9],[8,3,8,5,1],[7,6,5,4,3]]
det(matriz1)