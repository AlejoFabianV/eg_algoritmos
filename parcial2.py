'''
Se ingresa una frase, mostrar canitdad de veces que se repite cada vocal, cantidad de palabras, nro cantidad de @, "A"="a"
'''
# frase = str()
# largo_frase = int()
# cantidad_espacios = int()
# cantidad_palabras = int()
# c = int()
# ca = ce = ci = co = cu = especial = int()

# frase = input("ingrese frase: ")
# largo_frase = len(frase)
# for c in range(0, largo_frase):
#     if frase[c] == " ":
#         cantidad_espacios += 1
#         cantidad_palabras = cantidad_espacios + 1

#     match frase[c]:
#         case "A" | "a":
#             ca = ca + 1
#         case "E" | "e":
#             ce = ce + 1
#         case "I" | "i":
#             ci = ci + 1
#         case "O" | "o":
#             co = co + 1
#         case "U" | "u":
#             cu = cu + 1
#         case "@":
#             especial = especial +1
# print(frase, ca,ce,ci,co,cu, especial, largo_frase, cantidad_espacios,cantidad_palabras)

'''
Se ingresa una frase, convertir de la sig manera: primera letra de cada palabra en mayuscula, resto en minuscula
'''
# frase = str()
# largo_frase = int()
# senial = bool()
# auxi = str()
# x = int()

# frase = input("ingrese una frase: ").lower()
# largo_frase = len(frase)
# for x in range(0, largo_frase):
#     if senial == False:
#         auxi = auxi + frase[x].upper()
#         senial = True
#     else:
#         auxi = auxi + frase[x]
#         if frase[x] == " ":
#             senial = False
# frase = auxi        
# print(frase)


'''
Se ingresan datos de 100 alumnos (legajo, apellido, edad), Mostrar mayor edad, legajo y apellido del personas que tiene la mayor edad
'''

# elementos = 2
# vlegajo = [str()] * elementos
# vapellido = [str()] * elementos
# vedad = [int()] * elementos
# legajo = str()
# apellido = str()
# edad = int()
# x = int()
# maxiedad = int()

# for x in range(0, elementos):
#     legajo = input("ingrese nro legajo: ")
#     vlegajo[x] = legajo
#     apellido = input("ingrese apeliido: ")
#     vapellido[x] = apellido
#     edad = int(input("ingrese edad: "))
#     vedad[x] = edad
# for x in range(0,elementos):
#     if vedad[x] >= maxiedad:
#         maxiedad = vedad[x]
#         print(f'nro legajo {vlegajo[x]}, apellido {vapellido[x]}, edad mas grande {vedad[x]}')

'''
Cargar un vector de 100 elementos del tipo str con frases. Mostar: frase con mayor cantidad de palabras(puede repetirse)
'''
# def cantidad_palabras(pdatos):
#     cp = int()
#     x = int()
#     xx = int()
#     frase = str()
#     largo_frase = str()
#     vauxi = [int()] * 2

#     for x in range(0, 2):
#         frase = pdatos[x]
#         largo_frase = len(frase)
#         cp = 0
#         for xx in range(0, largo_frase):
#             if frase[xx] == " ":
#                 cp = cp + 1
#         vauxi[x] = cp
#     return(vauxi)

# def mayor(pauxi1):
#     elementos = 2
#     c = int()
#     mayor = int()
    
#     for c in range(0, elementos):
#         if pauxi1[c] > mayor:
#             mayor = pauxi1[c]
#     return(mayor)


# #prg.ppal
# elementos = 2
# auxi1 = [int()] * elementos
# vfrase = [str()] * elementos
# frase = str()
# x = int()

# for x in range(0, elementos):
#     frase = input("ingrese una frase: ")
#     vfrase[x] = frase
#     auxi1 = cantidad_palabras(vfrase)
#     maxi = mayor(auxi1)
# for x in range(0, elementos):
#     if auxi1[x] == maxi:
#         print(vfrase[x])

'''Diseñar una funcion que recibe una cadena como parametro de entrada con el sig formato:
cadena = apellido#ciudad#edad#especialidad#
Como se puede apreciar, el separador es el caracter #
Dicha funcion debera retornar un vector de 4 elementos tipo cadena desde:
elemento0 : apellido
elemento1: ciudad
elemento2: edad
elemento3: especialidad
crear un prg.ppaL que use esta funcion

'''

# def cadena(pfrase):
#     # pfrase = apellidp#ciudad#edad#especialidad
#     c = int()
#     e = int()
#     vi = int()
#     largo_frase = int()
#     vcadena = [str()] * 4
#     auxicad = str()

#     largo_frase = len(pfrase)
#     for c in range(0, largo_frase):
#         if pfrase[c] == "#":
#             auxicad = pfrase[vi:c]
#             vcadena[e] = auxicad
#             vi = c + 1
#             e = e + 1
#     auxicad = pfrase[vi:largo_frase]
#     vcadena[e] = auxicad
#     return(vcadena)

# #prg.ppal
# frase = str()
# x = int()
# vfrase = [str()] * 4

# frase = input("ingrese frase: ")
# vfrase = cadena(frase)
# for x in range(0,4):
#     print(vfrase[x])


'''
Crear funcion que recibre como parametro un vector de 50 elementos de Str() cargado con frases, Mostar: mostrar frases que tienen mayor cantidad de consonantes 
'''

'''
Crear una funcion que recibe una cadena como parametro de entrada, debera retornar la cantidad de veces que se repite cada vocal
sin discriminar entre mayusculas y minusculas
'''
# def vocales(pfrase):
#     x = int()
#     ca = ce = ci = co = cu = int()
#     largo_frase = int()

#     largo_frase = len(pfrase)
#     for x in range(0,largo_frase):
#         match pfrase[x]:
#             case "A":
#                 ca = ca + 1
#             case "E":
#                 ce = ce + 1
#             case "I":
#                 ci = ci + 1
#             case "O":
#                 co = co + 1
#             case "U":
#                 cu = cu + 1
#     return(ca,ce, ci, co, cu )

# frase = input("ingresa frase: ")
# frase = vocales(frase)
# print(frase)

'''
Cargar un vector int() de 100 elementos con numeros aleatorios comprenidos entre 1 y 1000, Mostar el vector ordenado
'''

# import random as r 
# elementos = 10
# vordenado = [int()] * elementos

# for x in range(0, elementos):
#     vordenado[x] = r.randint(1,1000)
# vordenado.sort()
# print(vordenado)

'''
Se ingresa con opcion a continuar los datos de las ventas realizadas por distinos venedores :
    NroVendedor int
    NroFactura  int
    FechaVenta  str[10]
    ImporteFactu real
El codigo del vendedor esta comprendido entre 1-30
Mostrar:
    Cantidad de ventas realizadas por cada nro de vendedor
    Total de importe por cada NroVendedor
    Promedio de importe facturado por cada NroVendedor
    NroVendedor con la mayor cantidad de ventas realizadas(puede ser un max repetido)
    NroVendedor con el mayor total de importe facturado(puede ser un max repetido)

'''
# nroVendedor = int()
# nroFactura = int()
# fechaVenta = [str()] * 10
# importeFactu = float()
# otro = str()

# max_v = [int()] * 31
# max_i = [int()] * 31
# x = int()
# maxiVentas = int()
# maxiImporte = int()
# vnroVendedorMayor = [int()]
# vnroVendedorMayorI = [int()]

# while otro != "n":
#     nroVendedor = int(input("ingrese nro de vendedor: "))
#     if nroVendedor >= 1 and nroVendedor <= 30:
#         nroFactura = int(input("Ingrese el nro de factura"))
#         fecha_venta = input("ingrese fecha [dd/mm/aaaa]: ")
#         max_v[nroVendedor] += 1
#         importeFactu = float(input("ingrese el importe de facturacion: "))
#         max_i[nroVendedor] += importeFactu
#     else:
#         print("nro de vendedor invalido")
    
#     otro = input("Quiere ingresar otro? ")

# for x in range(1,31):
#     if max_v[x] != 0:
#         promedio = max_i[x]/max_v[x]
#         print(f'Vendedor {x}, tiene {max_v[x]} venta/s y su importe es {max_i[x]}, su promedio es {promedio}')
#         if max_v[x] > maxiVentas:
#             maxiVentas = max_v[x]
#             vnroVendedorMayor = [x]
#         elif max_v[x] == maxiVentas:
#             vnroVendedorMayor.append(x)
#         if max_i[x] > maxiImporte:
#             maxiImporte = max_i[x]
#             vnroVendedorMayorI = [x]
#         elif max_i[x] == maxiImporte:
#             vnroVendedorMayorI.append(x)


# print(f'El vendedor/res con mayor ventas fue/ron {vnroVendedorMayor}, con {rep_v} ventas')
# print(f'El vendedor con mayor importe fue {vnroVendedorMayorI}')

'''
input con separacion
'''
# def cadena(pfrase):
#     largo = int()
#     x = int()
#     fecha_m = valor_m = int()
#     supervisor = turno = str()
#     vi = int()
#     e = int()
#     auxic = int()
#     vcad = [int()] * 4
    
#     largo = len(pfrase)
#     for x in range(0, largo):
#         if pfrase[x] == ";":
#             auxic = pfrase[vi:x]
#             vcad[e] = auxic
#             vi = x + 1 
#             e = e + 1
#     auxic = pfrase[vi:largo]
#     vcad[e] = auxic
#     fecha_m = vcad[0]
#     valor_m = vcad[1]
#     supervisor = vcad[2]
#     turno = vcad[3]

#     return(fecha_m, valor_m, supervisor, turno)

# frase = input("dd/mm/aaaa;valor;supervisor;turno : ")
# datos = cadena(frase)
# print(f'fecha: {datos[0]}, valor medio: {datos[1]}, supervisor: {datos[2]}, turno: {datos[3]}')

'''
Crear funcion que devueva la frase con mayor consonantes
'''
# def consonantes(pfrase):
#     largo = int()
#     frase = str()
#     car = int()
#     cc = int()
#     auxi = [int()] * 2
#     x = y = w = z = int()
#     maxi = int()

#     for x in range(0,2):
#         frase = (pfrase).upper()
#         largo = len(frase[x])
#         for y in range(0,largo):
#             car = ord(frase[y])
#             if car >= 65 and car <= 90:
#                 match frase[y]:
#                     case "A" | "E" | "I" | "O" | "U":
#                         print(" ")
#                     case _else :
#                         cc = cc + 1
#         auxi[x] = cc
#         cc = 0
#     for w in range(0,2):
#         if auxi[w] > maxi:
#             maxi = auxi[w]
#     for z in range(0,2):
#         if auxi[z] == maxi:
#             print(pfrase[z])
#     return

'''
Carga: debera permitir cargar un vector de 100 elementos con frases.
CantiPalabras: debera recibir un vector cargado como parametro y devolver un vector de 100 elementos del tipo 
               entero con la cantidad de palabras que tiene el vector de carga.
Imprimir: este modulo recibe como parametros el vector entero devuelto por CantiPlabras y debera mostrar los nro de elemento
          donde esta el mayor nro de palabras. (puede estar repetido)
Realizar programa principal.
'''

# def cantiPalabras(pfrase):
#     largo_frase = int()
#     frase = str()
#     vector_cp = [int()] * 100
#     cp = int()
#     y = x = int()
    
#     for x in range(0, 10):
#         frase = pfrase[x]
#         largo_frase = len(frase)
#         cp = 0
#         for y in range(0, largo_frase):
#             if frase[y] == " ":
#                 cp = cp + 1
#         vector_cp[x] = cp
#     return(vector_cp)

# def imprimir(pmaxi):
#     maxicp = int()
#     c = int()

#     for c in range(0,10):
#         if pmaxi[c] > maxicp:
#             maxicp = pmaxi[c]
#     return(maxicp)
    
# #prg.ppal
# frase = str()
# vfrase = [str()] * 100
# vauxi_cp = [int()] * 100
# mayor = int()
# x = int()

# for x in range(0,10):
#     frase = input("Ingrese una frase: ")
#     vfrase[x] = frase
#     vauxi_cp = cantiPalabras(vfrase)
#     mayor = imprimir(vauxi_cp)
# for x in range(0,10):
#     if vauxi_cp[x] == mayor:
#         print(f'la mayor frase esta en el elmento {x}')

'''
Se ingresan los datos de 200 empleados de una empresa:
    legajo: int
    sueldo: float
    fecha: str()
Mostar el legajo y sueldo de la persona con mayor antiguedad. (puede repetirse)
'''
def convertir(pfecha):
    fechastr = str()
    fechaint = int()

    fechastr = pfecha[6:] + pfecha[3:5] + pfecha[:2]
    fechaint = int(fechastr)
    return(fechaint)

legajo = int()
sueldo = float()
fecha = str()
vfecha = [int()] * 200
vlegajo = [int()] * 200
vsueldo = [float()] * 200
minf = 30000000

for x in range(0,2):
    legajo = int(input("legajo: "))
    sueldo = float(input("sueldo: "))
    fecha = input("fecha [dd/mm/aaaa]: ")

    vfecha[x] = convertir(fecha)
    if vfecha[x] <= minf:
        minf = vfecha[x]
        vlegajo[x] = legajo
        vsueldo[x] = sueldo
for x in range(0,2):
    if vfecha[x] == minf:
        print(f'legajo {vlegajo[x]}, sueldo {vsueldo[x]}, de la persona con mas antiguedad')