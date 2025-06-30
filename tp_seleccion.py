#2
'''print("Indice de masa corporal")
altura = float(input("Ingrese su altura: "))
peso = float(input("ingrese su peso: "))
indice_masa_corporal = peso / altura ** 2
print(indice_masa_corporal)

if indice_masa_corporal >= 18.5 and indice_masa_corporal <= 24.9:
    print("Esta en un peso saludable")
elif indice_masa_corporal < 18.5:
    print("Esta bajo de peso")
elif indice_masa_corporal > 24.9:
    print("Esta en sobrepeso")'''

#3
# nro = int(input("Ingrese un numero: "))
# if nro > 0:
#     raiz = nro ** 0.5
#     print(f"La raiz es: {raiz}")
# elif nro < 0:
#     modulo = nro * -1
#     raiz = modulo ** 0.5
#     print(f"La raiz es: {raiz}")
# else:
#     print("Usted ingreso un 0")

# 4
# edad = int(input("Ingrese su edad: "))
# sexo = input("Ingrese su sexo H o M: ")

# if (edad >= 65 and (sexo == "H" or sexo == "h")) or (edad >= 60 and (sexo == "M" or sexo == "m")):
#     print("se puede jubilar")
# else:
#     if sexo == "H" or sexo == "h":
#         restantes = 65 - edad
#         print(f"no se puede jubilar, le faltan {restantes} años")
#     elif sexo == "M" or sexo == "m":
#         restantes = 60 - edad
#         print(f"no se puede jubilar, le faltan {restantes} años")

#5 Desarrollar un programa que lea tres números y determine si pueden ser las medidas 
#de los lados de un triángulo. Si es así, determinar si es equilátero, isósceles o escaleno
'''medida_1 = int(input("Ingrese una medida"))
medida_2 = int(input("Ingrese una medida"))
medida_3 = int(input("Ingrese una medida"))

if medida_1 == medida_2 == medida_3:
    print("equilatero")
elif medida_1 == medida_2 != medida_3:
    print("isoceles")
elif medida_1 != medida_2 != medida_3:
    print("escaleno")'''

#6
'''import random as r 
jugada = input("Ingrese su jugada (piedra, papel o tijera): ")
jugada_aleatoria = r.randint(1,3)

if jugada_aleatoria == 1:
    print("Jugada del programa: piedra")
elif jugada_aleatoria == 2:
    print("Jugada del programa: papel")
elif jugada_aleatoria == 3:
    print("Jugada del programa: tijera")

match jugada:
    case "piedra":
        if jugada_aleatoria == 1:
            print("Empate")
        elif jugada_aleatoria == 2:
            print("Perdiste")
        elif jugada_aleatoria == 3:
            print("Ganaste")
    case "papel":
        if jugada_aleatoria == 1:
            print("Ganaste")
        elif jugada_aleatoria == 2:
            print("Empate")
        elif jugada_aleatoria == 3:
            print("Perdiste")
    case "tijera":
        if jugada_aleatoria == 1:
            print("Perdiste")
        elif jugada_aleatoria == 2:
            print("Ganaste")
        elif jugada_aleatoria == 3:
            print("Empate")'''

#7
nro1 = int(input("ingrse un nro: "))
nro2 = int(input("ingrese otro nro: "))
operacion = input("Indique que operacion desea realizar (S,R,M,D): ")

match operacion:
    case "S" | "s":
        suma = nro1 + nro2
        print(suma)
    case "R" | "r":
        resta = nro1 - nro2
        prtin(resta)
    case "M" | "m":
        multiplicacion = nro1 * nro2
        print(multiplicacion)
    case "D" | "d":
        if nro2 != 0:
            division = nro1 / nro2
        else:
            print("error, no se puede dividir por 0")
    case _:
        print("Operacion invalida")