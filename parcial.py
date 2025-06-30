# nro_micro = pasajeros = int()
# minp = 999999
# otro = str()
# z = int()
# litros = maxil = float()
# fecha_viaje = zona = destino = auxfecha = otro = str()
# #contadores
# cm1 = cm2 = cm3 = int()
# cpm1 = cpm2 = cpm3 = int()
# #acumuladores
# acup1 = acup2 = acup3 = int()
# acul1 = acul2 = acul3 = int()
# #promedios
# promedio1 = promedio2 = promedio3 = int()


# while otro != "n":
#     nro_micro = int(input("ingrese el nro de micro[1,2,3] "))
#     fecha_viaje = input("fecha del viaje ")
#     pasajeros = int(input("nro de pasajeros "))
#     destino = input("destino del viaje")
#     litros = float(input("cantidad de litros "))
#     zona = input("zona de viaje[S,C,N] ")
#     match nro_micro:
#         case 1:
#             cm1 = cm1 + 1
#             cpm1 = cpm1 + pasajeros
#             acup1 = acup1 + pasajeros
#             acul1 = acul1 + litros
#             promedio1 = acup1 / cpm1
#         case 2:
#             cm2 = cm2 + 1
#             cpm2 = cpm2 + pasajeros
#             acup2 = acup2 + pasajeros
#             acul2 = acul2 + litros
#             promedio2 = acup2 / cpm2
#         case 3:
#             cm3 = cm3 + 1
#             cpm3 = cpm3 + pasajeros
#             acup3 = acup3 + pasajeros
#             acul3 = acul3 + litros
#             promedio3 = acup3 / cpm3
    
#     if litros >= maxil:
#         maxil = litros
#         auxfecha = fecha_viaje

#     if pasajeros <= minp:
#         if pasajeros == minp:
#             z = z + 1
#         else:
#             minp = pasajeros
#             z = 1
#     otro = input("Quiere ingresar otro?[s o n] ")



# if cm1 > cm2 and cm1 > cm3:
#     print(cm1)
# elif cm2 > cm1 and cm2 > cm3:
#     print(cm2)
# elif cm3 > cm1 and cm3 > cm2:
#     print(cm3)

# print(cm1, cm2, cm3, promedio1, promedio2, promedio3, auxfecha)
# print(z)

legajo = int()
apellido = str()
categoria = str()
sexo = str()
h_cantidad = int()
sueldo = float()
otro = str()
ca = cb = cc = cm = int()
acusa = acusb = acusc = acusmp = promediospar = int()
auxlea = auxleb = auxlec = int()
auxaa = auxab = auxac = str()
maxs = int()

minsa = minsb = minsc = 99999
while otro != "N":
    legajo = int(input("legajo "))
    apellido = input("apellido ")
    categoria = input("categoria: ")
    sueldo = float(input("sueldo "))
    sexo = input("sexo ")
    match categoria:
        case "A":
            ca+=1
            acusa+=sueldo
            if sueldo < minsa:
                minsa = sueldo
                auxlea = legajo
                auxaa = apellido
        case "B":
            cb+=1
            acusb+=sueldo
            if sueldo < minsb:
                minsb = sueldo
                auxleb = legajo
                auxab = apellido
        case "C":
            cc+=1
            acusc+=sueldo
            if sueldo < minsc:
                minsc = sueldo
                auxlec = legajo
                auxac = apellido        
    if sexo == "M":
        if legajo % 2 == 0:
            cm+=1
            acusmp+=sueldo
            promediospar = acusmp / cm
    if sueldo >= maxs:
        if sueldo == maxs:
            z = z + 1
        else:
            maxs = sueldo
            z = 1
    otro = input("quiere ingresar otro? ")

print(ca,cb,cc, acusa,acusb,acusc,auxlea,auxleb,auxlec,z,promediospar)