#include <stdio.h>

int main(void) {
    float numero = 1, suma = 0;

    while (numero != 0) {
        printf("Introduce un número positivo (0 para terminar): ");
        scanf("%f", &numero);

        if (numero > 0) {
            suma = suma + numero;
        }
    }

    printf("La suma total es: %.2f\n", suma);

    return 0;
}
