'''se ingresan los datos de los empleados de una empresa:
    -legajo
    -apellido
    -categoria
    -sueldo
    -sexo
El ultimo tiene legajo = 99999 y no debe procesarce 
La categoria es una letra : A, B o C
El sexo: H o M
Mostrar: 
    -total de sueldos por cada categoria
    -cantidad de mujeres por cada categoria
    -cantidad de hombres por cada categoria
    -cantidad de personas con legajo par
    -cantidad de personas con legajo impar
    -promedio sueldo = acumulador / contador
'''
legajo = sueldo = int()
apellido = categoria = sexo = str()
#Contadores
contador = 0
contador_M_A = contador_M_B = contador_M_C = 0
contador_H_A = contador_H_B = contador_H_C = 0
contador_legajo_par = contador_legajo_impar = int()
#Acumulador
acumulador_sueldo_categoria_A = acumulador_sueldo_categoria_B = acumulador_sueldo_categoria_C = int()

legajo = int(input("Ingrese legajo: "))
while legajo > 0 and legajo < 99999:
    apellido = input("Ingrese apellido: ")
    categoria = input("Ingrese la categoria (A, B o C): ")
    sexo = input("Ingrese el sexo (M o H): ")
    sueldo = int(input("Ingrese el sueldo: "))
    
    #legajo par o inpar
    if legajo % 2 == 0:
        contador_legajo_par = contador_legajo_par + 1
    else:
        contador_legajo_impar = contador_legajo_impar + 1

    #hombres o mujeres por categoria
    if sexo == "M":
        if categoria == "A":
            contador_M_A = contador_M_A + 1
        elif categoria == "B":
            contador_M_B = contador_M_B + 1
        elif categoria == "C":
            contador_M_C = contador_M_C + 1
        else:
            print("categoria invalida")
    elif sexo == "H":
        if categoria == "A":
            contador_H_A = contador_H_A + 1
        elif categoria == "B":
            contador_H_B = contador_H_B + 1
        elif categoria == "C":
            contador_H_C = contador_H_C + 1
        else:
            print("categoria invalida")

    contador  = contador + 1

    #acumulador de sueldo por categoria
    if categoria == "A":
        acumulador_sueldo_categoria_A = acumulador_sueldo_categoria_A + sueldo
    elif categoria == "B":
        acumulador_sueldo_categoria_B = acumulador_sueldo_categoria_B + sueldo
    elif categoria == "C":
        acumulador_sueldo_categoria_C = acumulador_sueldo_categoria_C + sueldo

    legajo = int(input("Ingrese legajo: "))
promedio = (acumulador_sueldo_categoria_A + acumulador_sueldo_categoria_B + acumulador_sueldo_categoria_C) / contador

print(f"Total de sueldo por categoria A: {acumulador_sueldo_categoria_A}, B:{acumulador_sueldo_categoria_B}, C: {acumulador_sueldo_categoria_C}")
print(f"Cantidad de mujeres por categoria A: {contador_M_A}, B: {contador_M_B}, C: {contador_M_C}")
print(f"Cantidad de hombres por categoria A: {contador_H_A}, B: {contador_H_B}, C: {contador_H_C}")
print(f"Cantidad de legajos par: {contador_legajo_par}, legajos impares: {contador_legajo_impar}")
print(f"promedio sueldo {promedio}")