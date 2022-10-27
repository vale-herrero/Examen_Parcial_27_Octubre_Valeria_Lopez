
from heapq import merge


lista= [18, 50, 210, 80, 145, 333, 70, 30]

for numero in lista:
    if numero%10==0 and numero <200:
        print(numero)

print('---------------------')

for numero in lista:
    if numero<300:
        print(numero)
    else:
        break
print('---------------------')
def mergesort(lista):
    if len(lista)<=1:
        return lista
    else:
        medio =len(lista)//2
        izquierda=[]
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha=[]
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda=mergesort(izquierda)
        derecha=mergesort(derecha)
        if izquierda[medio-1]<=derecha[0]:
            izquierda+=derecha
            return izquierda
        resultado= merge(izquierda,derecha)
        return resultado
    
#mergesort(lista)

for i,numero in enumerate(lista):
    if lista[i] == 145:
        print(i)

