def menu():
    print("1. Conversión de temperatura")
    print("2. Tabla de multiplicar")
    print("0. Salir")

def conversion(a):

    convertido = (a*9/5+32)

    return convertido

def tabla (a):
    
    for i in range(11):
        resultado = int(i * a)
        print( a,"x",i,":", resultado)
    

opcion = 1

while opcion!=0:

        menu()
        opcion=int(input("Introduce Opción:"))

        match opcion:

            case 1:
                farenheit = int(input("Introduce temperatura en celsius: "))
                print("La temperatura farenheit es  ", conversion(farenheit))
            case 2:
                numero = int(input("Introduce numero para tabla de multiplicar hasta el 10: "))
                tabla(numero)

            case 0: print("Hasta luego...")
            case _: print ("Opción no valida")


