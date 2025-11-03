#include <stdio.h>


double suma(double a, double b, double c) {
    return a + b + c;
}

double multiplicacion(double a, double b, double c) {
    return a * b * c;
}

double resta(double a, double b, double c) {
    return a - b - c;
}


int main() {
    double num1, num2, num3;

    printf("Introduce tres numeros : ");
    scanf("%lf %lf %lf", &num1, &num2, &num3);

    printf("\nResultados:\n");
    printf("Suma: %.2lf\n", suma(num1, num2, num3));
    printf("Resta: %.2lf\n", resta(num1, num2, num3));
    printf("Multiplicacion: %.2lf\n", multiplicacion(num1, num2, num3));

    return 0;
}
