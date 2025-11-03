#include <stdio.h>
int main(void) {
int a, b;
printf("Introduce dos enteros (a b): ");
if (scanf("%d %d", &a, &b) != 2)
{
puts("Entrada invalida.");
return 1;
}
printf("Suma: %d + %d = %d\n", a, b, a + b);
printf("Resta: %d - %d = %d\n", a, b, a - b);
printf("Producto: %d * %d = %d\n", a, b, a * b);
if (b != 0) {
printf("Cociente ent.: %d / %d = %d\n", a, b, a / b); // division entera
printf("Resto: %d %% %d = %d\n", a, b, a % b);
printf("Cociente real: %d / %d = %.2f\n", a, b, (double)a / (double)b);
} else {
puts("Division por cero no permitida.");
}
return 0;
}