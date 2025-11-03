#include <iostream>
using namespace std;

int main() {
    int numero;
    int suma = 0;
    int contador = 0;
    cout << "Introduce numeros mayores que 0 (pulsa 0 para terminar): ";
    cin >> numero;

    while (numero != 0) {
        if (numero > 0) {
            suma += numero;
            contador++;
        }
        cout << "introduce otro numero (pulsa 0 para terminar): ";
        cin >> numero;
    }

    if (contador == 0) {
        cout << "No hay datos" << endl;
    } else {
        cout << "Suma total: " << suma << endl;
        cout << "Cantidad de numeros introducidos: " << contador << endl;
    }

    return 0;
}
