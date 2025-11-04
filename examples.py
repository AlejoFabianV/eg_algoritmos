# def binaria(pvector, pbusca):
#     central = int()
#     primero = ultimo = int()
#     senial = int()
#     nro = int()

#     senial = 0
#     primero = 0
#     ultimo = 999
#     while pbusca >= pvector[primero] and pbusca <= pvector[ultimo] and senial == 0:
#         central = (primero + ultimo)//2
#         if  pvector[central] == pbusca:
#             senial = 1
#             nro = central
#         elif pvector[central] > psbuca:
#             ultimo = central - 1
#         else:
#             primero = central + 1
#     if senial == 0:
#         nro = -1
#     reutrn(nro)

# def fibo(pnro):
#     if pnro == 1 or pnro == 2:
#         auxi = 1
#     else:
#         auxi = fibo(pnro - 2) + fibo(pnro-1)
#     return(auxi)
# print(fibo(5))

def factorial(pnro):
    if pnro == 1 or pnro == 0:
        auxi = 1
    else:
        auxi = factorial(pnro - 1) * pnro
    return(auxi)
print(factorial(1))

def utn(pc):
    if pc < 5:
        pc = pc + 1
        print('utn')
        utn(pc)
c = int()
utn(c)


# fila = 5
# col = 10
# m = [[float()] *col,[float()] *col,[float()] *col,[float()] *col,[float()] *col]
# nro = int()

# for x in range(0,5):
#     for y in range(0,10):
#         nro = int(input('nro: '))
#         m[x][y] = nro
# for y in range(0,10):
#     acu = 0
#     for x in range(0,5):
#         acu = acu + m[x][y]
#     print(acu)

    