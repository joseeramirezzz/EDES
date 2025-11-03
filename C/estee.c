#include <stdio.h>



int main(){
    float num1,num2,num3;
    float suma, resta, multiplicación;
    printf("Escribe primer numero: ");
    scanf("%f",&num1);
    printf("Escribe 2 numero: ");
    scanf("%f",&num2);
    printf("Escribe 3 numero: ");
    scanf("%f",&num3);

    suma = num1+num2+num3;
    resta = num1-num2-num3;
    multiplicación = num1*num2*num3;


    printf("suma: %.2f",suma);
    printf("\nresta: %.2f",resta);
    printf("\nmultiplicacion: %.2f",multiplicación);



}

