#include <stdio.h>

int main(void) {
    int numero;

    printf("Introduce un número entre 1 y 10: ");
    scanf("%d", &numero);


    if (numero < 1 || numero > 10) {
        printf("Error: el número debe estar entre 1 y 10.\n");
    } 
    else {
        printf("\nTabla de cuadrados hasta %d:\n", numero);
        for (int i = 1; i <= numero; i++) {
            printf("%d ^2 = %d\n", i, i * i);
        }
    }

    return 0;
}
