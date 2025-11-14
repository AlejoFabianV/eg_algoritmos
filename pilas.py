ele = int()
ele = 3
class Tpila:
    cima = int()
    datos = [int()] * ele

def inicializar(pila):
    pila.cima = -1
    return(pila)

def pilavacia(pila):
    aux = bool()
    if pila.cima == -1:
        aux = True
    else:
        aux = False
    return(aux)

def pilallena(pila):
    aux = bool()
    if pila.cima == (ele - 1):
        aux = True
    else:
        aux = False
    return(aux)

def agregar(pila, dato):
    if pilallena(pila) == True:
        print('pila llena')
    else:
        pila.cima = pila.cima + 1
        pila.datos[pila.cima] = dato
    return(pila)

def sacar(pila):
    if pilavacia(pila) == True:
        print('pila vacia')
    else:
        dato = pila.datos[pila.cima]
        pila.cima = pila.cima - 1
        print(dato)
    return(pila)

pilita = Tpila
inicializar(pilita)
otro = ape = str()
while otro != 'N':
    ape = input('apellido: ')
    agregar(pilita, ape)
    otro = input('quiere agregar otro? ')

otro = ''
while otro != 'N':
    sacar(pilita)
    otro = input('quiere sacar otro? ')