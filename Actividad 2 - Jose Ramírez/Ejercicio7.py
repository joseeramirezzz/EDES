numero = int(input("Escribe un número entero: "))  
# Pide al usuario que escriba un número y lo convierte a entero

factorial = 1  
# Creamos una variable para guardar el factorial, empezando en 1

for i in range(1, numero + 1):  
# Bucle que va desde 1 hasta el número que escribió el usuario

    factorial = factorial * i  
    # Multiplicamos el valor actual del factorial por el número i de cada vuelta

print("El factorial de ", numero, " es", factorial)  
# Muestra en pantalla el resultado final del factorial
