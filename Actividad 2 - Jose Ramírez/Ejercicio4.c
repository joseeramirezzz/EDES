#include <stdio.h>  

int main(void) {     

    int n = 1;       // Variable para guardar el número que introduce el usuario, inicializada en 1
    int suma = 0;    // Variable para guardar la suma de todos los números introducidos

    while (n != 0){  // Bucle que se repite mientras el usuario no escriba 0
        printf("Introduce un numero mayor que 0: ");   // Pide al usuario un número

        scanf("%d", &n);   // Guarda el número en la variable n

        if (n > 0){        // Comprueba que el número sea mayor que 0
            suma = suma + n;   // Si es mayor que 0, lo añade a la suma total
        } 
    }

    printf("La suma de los numeros introducidos es: %d ", suma);  
    // Muestra el resultado de la suma de todos los números introducidos
}
