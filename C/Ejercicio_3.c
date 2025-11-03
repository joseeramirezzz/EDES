#include <stdio.h>

int main(void) {
float nota;

printf("Introduce tu nota (0-10): ");
scanf("%f", &nota);

if (nota < 0 || nota > 10) {
    printf("Error: la nota debe estar entre 0 y 10.\n");
} 
else if (nota < 5) {
    printf("Insuficiente.\n");
} 
else if (nota < 6) {
    printf("Suficiente.\n");
} 
else if (nota < 7) {
    printf("Bien.\n");
} 
else if (nota < 9) {
    printf("Notable.\n");
} 
else {
    printf("Sobresaliente.\n");
}

return 0;
}
