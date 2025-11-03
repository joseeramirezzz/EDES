#include <stdio.h>

int main() {
    double base, altura, area, perimetro;

    printf("Escribe la base del rectángulo: ");
    scanf("%lf", &base);

    printf("Escribe la altura del rectángulo: ");
    scanf("%lf", &altura);

    area = base * altura;
    perimetro = 2 * (base + altura);

    printf("Área: %.3f\n", area);
    printf("Perímetro: %.3f\n", perimetro);

    return 0;
}
