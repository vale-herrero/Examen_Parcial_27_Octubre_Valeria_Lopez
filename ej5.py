
def crear_tabla(size):
    tabla = [None] * size

    return tabla

def funcion_hash(dato, tamanio_tabla):
    return dato % tamanio_tabla

def agregar(tabla, dato, convert):
    posicion = funcion_hash(ord(dato), len(tabla))

    if (tabla[posicion] is None):
        if convert:
            tabla[posicion] = convert8chr(dato)
        else:
            tabla[posicion] = dato
    else:
        print('se produjo una colision')

def convert8chr(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)

def binaryToDecimal(n):
    return int(n,2)

tabla1 = crear_tabla(126)
tabla2 = crear_tabla(126)


for i in range(32,126):
    agregar(tabla1, chr(i), convert = False)

for j in range(32,126):
    agregar(tabla2, chr(j), convert = True)

letra='E'
codification = tabla2[funcion_hash(ord(letra), len(tabla2))] 
dec = binaryToDecimal(codification)
caracter = tabla1[dec % len(tabla1)]

print(codification)
print(caracter)