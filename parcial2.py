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
Cargar un vector de 100 elementos del tipo str con frases. Mostar: frases con mayor cantidad de palabras(puede repetirse)
'''
elementos = 2
auxi1 = [int()] * elementos
vfrase = [str()] * elementos
frase = str()
x = int()

def cantidad_palabras(pdatos):
    cp = int()
    x = int()
    xx = int()
    frase = str()
    largo_frase = str()
    elementos = 2
    vauxi = [int()] * elementos

    for x in range(0, elementos):
        frase = pdatos[x]
        largo_frase = len(frase)
        cp = 0
        for xx in range(0, largo_frase):
            if frase[xx] == " ":
                cp = cp + 1
        vauxi[x] = cp
    return(vauxi)

def mayor(pauxi1):
    elementos = 2
    c = int()
    mayor = int()
    
    for c in range(0, elementos):
        if pauxi1[c] > mayor:
            mayor = pauxi1[c]
    return(mayor)



for x in range(0, elementos):
    frase = input("ingrese una frase: ")
    vfrase[x] = frase + " "
    auxi1 = cantidad_palabras(vfrase)
    maxi = mayor(auxi1)
for x in range(0, elementos):
    if auxi1[x] == maxi:
        print(vfrase[x])