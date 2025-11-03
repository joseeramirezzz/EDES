#include <stdio.h>

int main() {
    float celsius, fahrenheit;

    printf("Escribe los grados Celsius: ");
    scanf("%f", &celsius);

    fahrenheit = celsius * 9 / 5 + 32;

    printf("En Fahrenheit es: %.2f\n", fahrenheit);

    return 0;
}
