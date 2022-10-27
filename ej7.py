
class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self,valor,termino):
        self.valor= valor
        self.termino=termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor= None
        self.grado= -1

def agregartermino(polinomio, termino, valor):
    aux= Nodo()
    dato= datoPolinomio(valor, termino)
    aux.info= dato
    if termino > polinomio.grado:
        aux.sig= polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado= termino
    else:
        actual= polinomio.termino_mayor
        while (actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig
        aux.sig= actual.sig
        actual.sig=aux

def modificar_termino(polinomio, termino, valor):
    "modifica un termino del polinomio"
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino != termino:
        aux=aux.sig
    aux.info.valor = valor

def obtener_valor(polinomio, termino):
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:   
        aux=aux.sig
    if aux is not None and aux.info.termino == termino:  
        return aux.info.valor
    else:
        return 0

def restar(polinomio1, polinomio2):
    paux= Polinomio()
    mayor= polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
    for i in range(0, mayor.grado +1):
        total = obtener_valor(polinomio1, i) - obtener_valor(polinomio2, i)
        if total !=0:
            agregartermino(paux,i,total)
    return paux

def dividir(polinomio1, polinomio2):
    paux=Polinomio()
    pol1= polinomio1.termino_mayor
    mayor= polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
    while pol1 is not None:
        pol2 = pol2.termino_mayor
        while pol2 is not None:
            termino = pol1.info.termino - pol2.info.termino
            valor= mayor/pol2.info.valor
            if (obtener_valor(paux, termino)!=0):
                valor-=obtener_valor(paux,termino)
                modificar_termino(paux,termino,valor)
            else:
                agregartermino(paux,termino, valor)
            pol2=pol2.sig
        pol1=pol1.sig
    return paux

def eliminar(polinomio, clave):
    dato = None
    if polinomio.termino_mayor.info == clave:
        dato = polinomio.termino_mayor.info
        polinomio.termino_mayor= polinomio.termino_mayor.sig
        polinomio.termino_mayor -=1
    else:
        anterior= polinomio.termino_mayor
        actual= polinomio.termino_mayor.sig
        while actual is not None and actual.info != clave:
            anterior= anterior.sig
            actual= actual.sig
        if actual is not None:
            dato= actual.info
            anterior.sig = actual.sig
            polinomio.termino_mayor -=1
    return dato

def encontrar_valor(polinomio, termino):
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:   
        aux=aux.sig
    if aux is not None and aux.info.termino == termino:  
        return aux.info.valor
    else:
        return 0