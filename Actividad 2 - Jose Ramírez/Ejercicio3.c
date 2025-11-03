#include <stdio.h>   

int main (void) {   

    int b;   // Variable donde guardaremos el número que pida el usuario
    int a;   // Variable que usaremos como contador en el bucle

    printf ("Introduce un numero del 1 al 10: ");   // Muestra un mensaje para pedir un número

    scanf("%d", &b);   // Lee el número que escribe el usuario y lo guarda en la variable b

    if ( b >= 1 && b <= 10 ){   // Comprueba que el número esté entre 1 y 10

        for (a = 1; a <= 10; a++){   // Repite el bloque de código desde a=1 hasta a=10
            printf ("%d x %d = %d \n ", b, a, a*b);   // Imprime la tabla de multiplicar del número b
        }	

    } else {   // Si el número no está entre 1 y 10
        printf ("Escribe un numero entre el 1 y el 10");   // Muestra este mensaje
    }

}   
