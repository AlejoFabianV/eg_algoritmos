#Estructura de casos
#nro_mes = int(input("Ingrese nro de mes: "))

'''match nro_mes: 
    case 1 | 2 | 3 | 4:
        print("primer cuatri")
    case 5 | 6 | 7 | 8:
        print("segundo cuatri")
    case 9 | 10 | 11 | 12:
        print("tercer cuatri")
    case _:
        print("mes inexistente")'''

#AyED
#25/04
#Autor: Verhagen Alejo
nombre_materia = input("Ingrese el nombre de la materia: ")
nota = int(input("ingrese su nota: "))

if nota >= 4 and nota <= 10:
    print(f'En la materia {nombre_materia}, esta Aprobado')
    match nota:
        case 4 | 5 | 6:
            print("Bien")
        case 7 | 8:
            print("Muy bien")
        case 9:
            print("excelente")
        case _:
            print("Brillante")
elif nota > 10:
    print("Nota invalida")
else:
    print(f"En la materia {nombre_materia}, esta Desaprobado")
    match nota:
        case 1 | 2 | 3:
            print("Recupera")