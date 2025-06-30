#AyED
#23/05
#Verhagen Alejo
# edad = maxie = x = int()

# while x < 5:
#     edad = int(input("ingrese una edad: "))
#     x += 1
#     if edad > maxie:
#         maxie = edad
# print(f"Edad mas grende: {maxie} años")

import random as r
nro = maxin = x = int()

maxn = -10000
while x < 100:
    x += 1
    nro = r.randint(-50,-10)
    if nro > maxn:
        maxn = nro
print(f"Mayor nro: {maxn}")