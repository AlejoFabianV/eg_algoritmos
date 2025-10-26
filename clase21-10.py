#Devolver el acumulado de numeros - RECURSIVIDAD
'''def acumular(pc, pa):
    x = int()
    if pc < 5:
        pc = pc + 1
        nro = int(input("nro: "))
        pa = pa + nro
        x = acumular(pc, pa)
    else:
        x = pa
    return(x)
#prg ppal
c = a = y = int()
y = acumular(c, a)
print(y)'''

#Mezclar vectores - MERGE
#Teniendo dos vectores ordenadors generas un tercero ordenado sin aplicar metodo de insercion o burbuja 

#ej tipo parcial
'''a = [int()] * 4
b = [int()] * 6
c = [int()] * 10
xa = xb = int()
e = int()
z = int()

#carga y orden de a y b (suponiendo ya listo)
a[0] = 10
a[1] = 12
a[2] = 20
a[3] = 30

b[0] = 11
b[1] = 25
b[2] = 28
b[3] = 60
b[4] = 80
b[5] = 100
while xa < 4 and xb < 6:
    if a[xa] < b[xb]:
        c[z] = a[xa]
        xa = xa + 1
    else:
        c[z] = b[xb]
        xb = xb + 1
    z = z + 1

if xa == 4:
    for e in range(xb, 6):
        c[z] = b[e]
        z = z + 1
else:
    for e in range(xa, 4):
        c[z] = a[e]
        z = z + 1
for e in range(0, 10):
    print(c[e])'''

#Sentencia separar - SPLIT
#dado un var cadena, generar un vector con el contenido de la misma

#En DF: vector = SEPARAR(varcadena, "separador que se esta usando")
#ej separador: '#' ';'

'''alumno = input('alumno: ')
datos = alumno.split("#")
print(datos)'''
#en este caso datos es un vector

#se tiene una var cadena: legajo;apellido;especialidad;edad
#ej: 1000;lopez;Q;22 separador ';'
#crear un vector con de 4 elementos del tipo string con los datos de la variable

'''datos = [str()] * 4
frase = str()
x = int()

frase = input('dato: ')
datos = frase.split(';')
for x in range(0, 4):
    print(datos[x])'''

#ARCHIVOS
#conjunto de registros que esta grabado en una memoria permanente
#Un registro es un conjunto de campos, un campo es el lugar donde queda grabado un dato

#temas a tratar:
#   Crear ARCHIVOS
#   Leer ARCHIVOS
#   Consultar un registro
#   Modificar/Borrar un registro
#   Agregar registros

#A-B-M Altas-Bajas-Modificaciones -> enfocado en la parte de modificar/borrar/agregar registros

#ABRIR ARCHIVO
'''vararchivo = open('nombre.ext','modo')'''
#El modo es una letra que implica que queres hacer con el archivo
# w: crear el archivo (si existe el archivo lo borra)
# r: leer el archivo
# a: agregar registros 

#en DF
'''varalu = ABRIR('alu.dat', 'w')'''

#en PY
'''varalu = open('alu.dat','w')'''
#varalu es tambien el nomobre interno del archivo, alu.dat es el nombre externo del archivo

#CERRAR ARCHIVO
#todo archivo que fue abierto debe ser cerrado, una implicacion muy importante es que los registros no quedan guardados

#en DF
'''CERRAR(vararchivo)'''

#en PY
'''vararchi.close()'''