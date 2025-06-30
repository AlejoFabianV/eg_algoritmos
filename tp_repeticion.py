#1
# nro = int(input("Ingrese un nro "))
# factorial = 1
# control = int()

# for control in range(1, nro + 1):
#     factorial = factorial * control 
#     print(factorial)

#3
#Se ingresan los datos de la producción de litio:  
#✓ FechaProdu string[10] (dd/mm/aaaa) 
#✓ ToneProd real 
#✓ Turno  char 
#El turno es una letra M, T o N (mañana, tarde y noche respetivamente) 
#La ultima producción tiene como fecha de producción 99/99/9999 y no debe procesarse. 
#Imprimir: 
#• Cantidad de producciones realizadas en cada turno. 
#• Total de toneladas producidas en cada turno. 
#• Promedio de toneladas producidas. 
#• Letra del turno donde se obtuvo el mayor promedio de toneladas producidas.

# fechaprod = turno = str()
# toneprod = float()
# #contadores
# cm = ct = cn = int()
# #acumuladores
# acutm = acutt = acutn = int()
# promediotm = promediott = promediotn = int()

# fechaprod = input("Ingresa la fecha[dd/mm/yyyy] ")
# while fechaprod > "00/00/0000" and fechaprod < "99/99/9999":
#     turno = input("turno [M,T,N]")
#     toneprod = float(input("toneladas producidas "))
#     match turno:
#         case "M":
#             cm = cm + 1
#             acutm = acutm + toneprod
#             promediotm = acutm / cm
#         case "T":
#             ct = ct + 1
#             acutt = acutt + toneprod
#             promediott = acutt / ct
#         case "N":
#             cn = cn + 1
#             acutn = acutn + toneprod
#             promediotn = acutn / cn
    
#     fechaprod = input("Ingrese una fehca de prod")

# if promediotm > promediotn and promediotm > promediott:
#     print("mañana")
# elif promediott > promediotm and promediott > promediotn:
#     print("tarde")
# elif promediotn > promediotm and promediotn > promediott:
#     print("noche") 
# print(cm, ct, cn, acutm, acutt, acutn, promediotm, promediott, promediotn)






#5 Se ingresa con opción a continuar los datos de los alumnos que cursan en la UTN Delta: 
# ✓ Apellido String[15] 
# ✓ Legajo  Integer
# ✓ Edad  Integer  
# ✓ Especialidad Char 
# ✓ Sexo  Char 
# La especialidad es una letra: Q, M, E o S (química, mecánica, eléctrica y sistemas 
# respectivamente) 
# El sexo es una letra: M o H (Mujer o Hombre) 
# Imprimir: 
# • Cantidad de personas por cada especialidad 
# • Promedio de edad por cada especialidad 
# • Menor edad de los hombres por cada especialidad 
# • Menor edad de las mujeres por cada especialidad 
# • Cantidad de legajos pares por cada especialidad 
# • Cantidad de legajos impares por cada especialidad 
# • Letra de la especialidad donde se encuentra el mayor promedio de edad. 

apellido = especialidad = sexo = str()
legajo = edad = int()
#contadores
cq = cpar = cimpar = int()
mineh = minem =  q = int()
#acumuladores 
acueq = int()
promedioeq = int()

legajo = int(input("ingrese nro de legajo"))
while legajo != 0:
    apellido = input("apellido ")
    especialidad = input("especialidad[Q,M,E o S] ")
    edad = int(input("ingrese la edad "))
    sexo = input("ingrese el sexo[H o M] ")
    match especialidad:
        case "Q":
            cq = cq + 1
            acueq = acueq + edad
            promedioeq = acueq / cq
            if legajo % 2 == 0:
                cpar = cpar + 1
            else:
                cimpar = cimpar + 1
            match sexo:
                case "H":
                    if edad <= mineh:
                        if edad == mineh:
                            q = q + 1
                        else:
                            mineh = edad
                            q = 1
                case "M":
                    if edad <= minem:
                        if edad == minem:
                            q = q + 1
                        else:
                            minem = edad
                            q = 1
    legajo = int(input("Quiere ingresar otro legajo?[0 = no] "))

print(cq, acueq, mineh, minem, cpar, cimpar, q, promedioeq)

