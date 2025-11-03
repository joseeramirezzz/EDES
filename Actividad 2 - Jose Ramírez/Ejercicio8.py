numero1 = int(input("Introduzca un número: "))  
# Pide al usuario el primer número y lo convierte a entero

numero2 = int(input("Introduzca otro número: "))  
# Pide al usuario el segundo número y lo convierte a entero

suma = numero1 + numero2  
# Calcula la suma de los dos números

resta = numero1 - numero2  
# Calcula la resta del primero menos el segundo

multiplicacion = numero1 * numero1  
# Calcula la multiplicación del primer número por sí mismo (ojo, no es numero1*numero2)

if numero1 == 0 or numero2 == 0:  
# Comprueba si alguno de los dos números es 0
    print("La suma de los dos numeros es:", suma, " la resta ", resta, " la multiplicación ", multiplicacion, " y no se puede dividir entre 0.")  
    # Si alguno es 0, muestra la suma, la resta, la multiplicación y un aviso de que no se puede dividir entre 0
else:  
    division = numero1 / numero2  
    # Si ninguno es 0, calcula la división del primero entre el segundo
    print("La suma de los dos numeros es:", suma, " la resta ", resta, " la multiplicación ", multiplicacion, " y la division", division)  
    # Muestra todos los resultados incluyendo la división
