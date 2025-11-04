'''VECTORES CONTADORES Y ACUMULADORES'''
#se ingresa con opcion a continuar producciones de hornos
# nrohorno (1-20)
# toneladas
# fecha
#mostrar: cantidad de producciones por cada horno, total de toneladas por cada horno, total de toneladas por mes, nro mes con mayor total de producciones (repetida)

# nro_horno = int()
# tone = float()
# fecha = str()
# produ_horno = [int()] * 21
# tone_horno = [int()] * 21
# tone_mes = [int()] * 21
# fechastr = str()
# fechaint = int()
# maxiprod = int()
# otro = str()

# while otro != 'N':
#     nro_horno = int(input('nro horno: '))
#     tone = float(input('toneladas: '))
#     fecha = input('ingrese fecha: ')

#     fechastr = fecha[3:5]
#     fechaint = int(fechastr)
#     tone_mes[fechaint] = tone_mes[fechaint] + tone 
#     produ_horno[nro_horno] = produ_horno[nro_horno] + 1
#     tone_horno[nro_horno] = tone_horno[nro_horno] + tone
#     otro = input('quiere ingresar otro? ')
# for x in range(1,21):
#     print(produ_horno[x])
#     print(tone_horno[x])
# for x in range(1,21):
#     if tone_mes[x] > maxiprod:
#         maxiprod = tone_mes[x]
# for x in range(1,21):
#     if tone_mes[x] == maxiprod:
#         print(x)

'''VECTORES ORDENADOS: INSERCION Y BURBUJA'''

'''Insercion'''
# v = [int()] * 5
# nro = int()
# barrido = int()
# ev = ef = int()
# for x in range(0,5):
#     nro = int(input('numero: '))
#     v[x] = nro
# for x in range(0,5):
#     barrido = barrido + 1
#     ev = ef 
#     while ev < 4:
#         ev = ev + 1
#         if v[ef] > v[ev]:
#             auxi = v[ef]
#             v[ef] = v[ev]
#             v[ev] = auxi
#     ef = ef + 1 
# for x in range(0,5):
#     print(v[x])

'''Burbuja '''
# v = [int()] * 5
# ea = es = int()
# barrido = int()
# nro = int()
# ultimo = int()
# for x in range(0,5):
#     nro = int(input('nro: '))
#     v[x] = nro
# for x in range(0,5):
#     barrido = barrido + 1
#     ea = 0
#     ultimo = 5 - barrido 
#     while ea < ultimo:
#         es = ea + 1
#         if v[ea] > v[es]:
#             auxi = v[ea]
#             v[ea] = v[es]
#             v[es] = auxi
#         ea = ea + 1
# for x in range(0,5):
#     print(v[x])


'''Busquedas en vectores ordenados - INDEXADA O BINARIA '''
#Ya teniendo un vector ordenado por cualquier metodo

'''INDEXADA'''
#Crear una funcion con paramatros de entrada (vector ordenado y dato a buscar), debera devolver el nro de elementos donde se encuentrael dato
# def index(porden, pbusca):
#     x = int()
#     senial = int()
#     nro = int()

#     senial = 0
#     nro = -1
#     while x < 5 and senial == 0:
#         if porden[x] == pbusca:
#             nro = x
#             senial = 1
#         elif porden[x] > pbusca:
#             senial = 1
#         x = x + 1
#     return(nro)

# datos = index([1,2,3,4,5],5)
# print(datos)

'''BINARIA'''
# def binaria(porden, pbusca):
#     x = int()
#     senial = int()
#     central = int()
#     primero = ultimo = int()
#     nro = int()

#     primero = 0
#     ultimo = 6
#     while pbusca >= porden[primero] and pbusca <= porden[ultimo] and senial == 0:
#         central = (primero + ultimo)// 2
#         if porden[central] == pbusca:
#             nro = central
#             senial = 1
#         elif porden[central] > pbusca:
#             ultimo = central - 1
#         else: 
#             primero = central + 1
#     if senial == 0:
#         nro = -1
#     return(nro) 

# datos = binaria([1000,2000,3500,4500,5000,6000,7000],4500)
# print(datos)

'''MATRICES'''

#Cargar una matriz por fila
# fila = 4
# col = 3
# m = [[int()] *col,[int()] *col,[int()] *col,[int()] *col]
# dato = int()
# for x in range(0,4):
#     for y in range(0,3):
#         dato = int(input('nro: '))
#         m[x][y] = dato
# for x in range(0,4):
#     for y in range(0, 3):
#         print(m[x][y])

'''RECURSIVIDAD'''

#Fibonacci
# def fibo(pnro):
#     if pnro == 1 or pnro == 2:
#         aux = 1
#     else:
#         aux = fibo(pnro - 2)+ fibo(pnro - 1)
#     return(aux)
# print(fibo(2))

# def factorial(pnro):
#     if pnro == 1 or pnro == 0:
#         auxi = 1
#     else:
#         auxi = factorial(pnro - 1) * pnro
#     return(auxi)
# print(factorial(1))

# def utn(pc):
#     if pc < 5:
#         pc = pc + 1
#         print('utn')
#         utn(pc)
# c = int()
# utn(c)

'''ARCHIVOS: Corte de control'''
#se tiene un archivo de produccion aceros.dat
# registro:
#   fechaprod
#   nrohorno
#   toneprod
#el archivo esta ordenado por nrohorno
#mostrar: cantidad de producciones por horno y total de toneladas producidas

# def campos(pregis):
#     v = [str()] * 3
#     v = pregis.split() 
#     return(v)

# regis = str()
# vector = [int()] * 3
# arhivo = open('acero.txt', 'r')
# regis = archivo.readline()
# vector = campos(regis)
# cfecha = vector[0]
# cnrohorno = str(vector[1])
# ctoneprod = str(vector[2])

# while regis != '':
#     control = cnrohorno
#     z = 0 
#     acu = 0
#     while regis != '' and control == nrohorno:
#         z = z + 1
#         acu = acu + ctoneprod
#         regis = archivo.readline()
#         if regis != '':
#             vector = campos(regis)
#             cfecha = vector[0]
#             cnrohorno = str(vector[1])
#             ctoneprod = str(vector[2])
#     print(control,z,acu)
# archivo.close()

'''ARCHIVOS: PROGRAMA DE ALTAS CON VERIFICACION DE EXISTENCIA'''
regis = str()
lega = int()
ape = str()
espe = str()
senial = 0

#archi = open('alu.dat', 'w')
archi = open('alu.dat', 'r')
lega = int(input('lega: '))
ape = input('ape: ')
espe = input('espe: ')
regis = archi.readline().rstrip()

while regis != '' and senial == 0:
    v = regis.split(';')
    relega = int(v[0])
    reape = v[1]
    reespe = v[2]
    if lega == relega:
        print('legajo existente')
        senial = 1
    regis = archi.readline().rstrip()
archi.close()
if senial == 0:
    archi = open('alu.dat','a')
    regis = str(lega) + ';' + ape + ';' + espe + '\n'
    archi.write(regis)
    archi.close()

