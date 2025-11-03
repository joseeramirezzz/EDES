#include <stdio.h>


int factorial(int a) {
    int n = 1;
    int i;

    for (i = 1; i <= a; i++) {
        n = n * i;
    }
    return n;
}


int resto(int a, int b) {
    return a % b;
}

int main() {
    int numero1, numero2;

    printf("Escribe dos numeros enteros: ");
    scanf("%d %d", &numero1, &numero2);

    printf("\nFactorial de %d : %d", numero1, factorial(numero1));
    printf("\nFactorial de %d : %d", numero2, factorial(numero2));
    printf("\nResto : %d\n", resto(numero1, numero2));

    return 0;
}
