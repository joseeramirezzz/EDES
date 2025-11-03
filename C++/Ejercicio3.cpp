#include <iostream>
using namespace std;


double sumar(double a, double b) {
    return a + b;
}

double restar(double a, double b) {
    return a - b;
}

double multiplicar(double a, double b) {
    return a * b;
}

double dividir(double a, double b) {
    if (b == 0) {
        cout << "Error: no se puede dividir entre 0." << endl;
        return 0;
    }
    return a / b;
}

int main() {
    double num1, num2;

    cout << "Introduce el primer numero: ";
    cin >> num1;
    cout << "Introduce el segundo numero: ";
    cin >> num2;

    cout << endl;
    cout << "Suma: " << sumar(num1, num2) << endl;
    cout << "Resta: " << restar(num1, num2) << endl;
    cout << "Multiplicacion: " << multiplicar(num1, num2) << endl;
    cout << "Division: " << dividir(num1, num2) << endl;

    return 0;
}
