#CLASE 12/09
'''
Vector contador o Vector acumulador

vector[elemento] = vector[elemento] + 1  -> VECTOR CONTADOR
el elemento es un dato ingresado por el usuario

vector[elem] = vecror[elem] + var a sumar  -> VECTOR CONTADOR
'''

'''
Se ingresa con opcion a continuar nro de horno, fecha de produccion y toneladas, y el nro de horno es un nro: 1-10
Mostrar 
    cantidad de producciones de cada horno
    total de toneladas producidas por cada horno
    mayor/menor en vector contador
'''
# nro_horno = int()
# fecha_prod = str()
# toneladas = float()
# otro = str()
# cantidad_producciones = [int()] * 11 #ya que no vamos a trabajar con elemento 0 
# toneladas_producidas = [float()] * 11
# maxi = int()


# while otro != "n":
#     nro_horno = int(input("ingrese nro de horno: "))
#     fecha_prod = input("ingrese la fecha: ")
#     toneladas = float(input("ingrese toneladas: "))
#     cantidad_producciones[nro_horno] = cantidad_producciones[nro_horno] + 1
#     toneladas_producidas[nro_horno] = toneladas_producidas[nro_horno] + toneladas

#     otro = input("Quiere ingresar otro?: ")

# for x in range(1,11):
#     if cantidad_producciones[x] != 0: #opcional ya que puedo querer todos los datos solo por verificacion
#         print(f'nro de horno {x},cantidad produccion {cantidad_producciones[x]}, toneladas producidas: {toneladas_producidas[x]}')
# for x in range(1,11):
#     if cantidad_producciones[x] > maxi:
#         maxi = cantidad_producciones[x]
# print(f'max cantidad producciones {maxi}')
# for x in range(1,11):
#     if cantidad_producciones[x] == maxi:
#         print(f'maxi cantidad producciones {x}')

#TIPO PARCIAL 3
'''
Se ingresa con opcion a continuar los viajes realizados por micros de larga distancia
Datos:
    fecha: str
    nro_micro: int
    cantidad_pasajeros: int
nro de mirco comprendido entre 1-50
Mostar:
    -cantidad de viajes realizados por cada micro
    -total de pasajeros transportados por cada micro
    -nro de micro con la myor canitdad de viajes(puede estar repetido)
    -nro de micro con el mayor total de pasajeros transportados(puede estar repetido)
    -promedio de pasajeros transportados por cada viaje por cadad micro
'''
fecha = str()
nro_micro = int()
cantidad_pasajeros = int()
otro = str()
total_pasajeros = [int()] * 51
cantidad_viajes = [int()] * 51
promedio_pasajeros = [int()] * 51
maxv = int()
maxtp = int()

while otro != "n":
    nro_micro = int(input("ingrese nro micro: "))
    cantidad_pasajeros = int(input("cantidad de pasajeros: "))
    cantidad_viajes[nro_micro] = cantidad_viajes[nro_micro] + 1
    total_pasajeros[nro_micro] = total_pasajeros[nro_micro] + cantidad_pasajeros
    promedio_pasajeros[nro_micro] = total_pasajeros[nro_micro] / cantidad_viajes[nro_micro]

    otro = input("quiere ingresar otro viaje: ")

for x in range(1,51):
    print(f'micro: {x}, cantidad de viajes {cantidad_viajes[x]}, total de pasajeros {total_pasajeros[x]}')
    print(f'promedio de pasajeros {promedio_pasajeros[x]}')
for x in range(1,51):
    if cantidad_viajes[x] > maxv:
        maxv = cantidad_viajes[x]
    if total_pasajeros[x] > maxtp:
        maxtp = total_pasajeros[x]
print(f'max viajes {maxv}, total pasajeros max {maxtp}')
for x in range(1,51):
    if cantidad_viajes[x] == maxv:
        print(f'maximo de viajes micro: {x}')
    if total_pasajeros[x] == maxtp:
        print(f'total de pasajeros max para el micro: {x}')