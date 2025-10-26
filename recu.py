'''
Se ingresan los datos de 5mil estudiantes 
    legajo
    apellido
    edad
    sexo
mostrar:
    legajo, apellido de los hombres de mayor edad(puede repetirse)
    legajo, apellido de las mujeres de mayor edad(puede repetirse)
'''

# legajo = int()
# ape = str()
# edad = int()
# sexo = str()
# vlega = [int()] * 3
# vape = [str()] * 3
# vedad = [int()] * 3
# vsexo = [str()] * 3
# maxeh = maxem = int()
# axuapeh = axuapem = str()
# auxilegah = auxilegam = int()

# for x in range(0,3):
#     legajo = int(input("ingrese legajo: "))
#     ape = input("ingrese su ape: ")
#     edad = int(input("edad: "))
#     sexo = input("sexo [M o H]")
#     vlega[x] = legajo
#     vape[x] = ape
#     vedad[x] = edad
#     vsexo[x] = sexo

# for x in range(0,3):
#     if vsexo[x] == "H":
#         if vedad[x] > maxeh:
#             maxeH = vedad[x]
#             axuapeh = vape[x]
#             auxlegah = vlega[x]
#     elif vsexo[x] == "M":
#         if vedad[x] > maxem:
#             maxem = vedad[x]
#             axuapem = vape[x]
#             auxlegam = vlega[x]
# for x in range(0,3):
#     if vsexo[x] == "H":
#         if vedad[x] == maxeh:
#             print(x)
#     elif vsexo[x] == "M":
#         if vedad[x] == maxem:
#             print(x)
# print(f'h {axuapeh}, lega {auxlegah}')
# print(f'h {axuapem}, lega {auxlegam}')

'''
Carga: debera permitir cargar un vector de 100 elementos con frases.
CantiPalabras: debera recibir el vector cargado como parametro y devolver un vector de 100 elementos del tipo 
               entero con la cantidad de palabras que tiene el vector de carga.
Imprimir: este modulo recibe como parametros el vector entero devuelto por CantiPlabras y debera mostrar los nro de elemento
          donde esta el mayor nro de palabras. (puede estar repetido)
Realizar programa principal.
'''

# def carga():
#     frases = str()
#     vfrase = [str()] * 2

#     for x in range(0,2):
#         frases = input("frase: ")
#         vfrase[x] = frases
#     print(vfrase)
#     return(vfrase)

# def cantiPalabras(pfrase):
#     frase = str()
#     largo_frase = int()
#     auxip = [int()] * 2
#     x = int()
#     y = int()
#     cp = int()

#     for x in range(0,2):
#         frase = pfrase[x]
#         largo_frase = len(frase)
#         cp = 0
#         for y in range(0,largo_frase):
#             if frase[y] == " ":
#                 cp = cp + 1
#         auxip[x] = cp
#     return(auxip)

# def imprimir(pcp):
#     maxcp = int()
#     elem = int()

#     for x in range(0,2):
#         if pcp[x] >= maxcp:
#             maxcp = pcp[x]
#             elem = x
#     print(f'elemento con mas palabras {elem}')

# def main():
#     frase = carga()
#     canti_palabras = cantiPalabras(frase)
#     imprimir(canti_palabras)

# main()

'''
se ingrsean 200 empleados
legajo
sueldo 
fecha ingreso
Mostrar legajo y sueldo del de mayor antiguedad (puede ser repetido)
'''

def convertir(pfecha):
    fechastr = str()
    fechaint = int()

    fechastr = pfecha[6:] + pfecha[3:5] + pfecha[:2]
    fechaint = int(fechastr)
    return(fechaint)

lega = int()
sue = float()
fecha = str()
x = int()
elementos = 2
vfecha = [int()] * elementos
vlega = [int()] * elementos
vsue = [float()] * elementos
anti = int()
alega = int()
asue = int()

anti = 99999999
for x in range(0,elementos):
    lega = int(input("legajo: "))
    sue = float(input("sueldo: "))
    fecha = input("fecha dd/mm/aaaa ")

    vfecha[x] = convertir(fecha)
    vlega[x] = lega
    vsue[x] = sue
    if vfecha[x] < anti:
        anti = vfecha[x]
        alega = vlega[x]
        asue = vsue[x]
        

for x in range(0,elementos):
    if vfecha[x] == anti:
        print(x, vlega[x], vsue[x])
print(f'mayor antiguedad {alega}, {asue}')

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

