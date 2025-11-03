#include <iostream>
using namespace std;

int main() {
    string nombre;
    int N;

    cout << "Introduce nombre: ";
    cin >> nombre;

    cout << "introduce numero entre 1 y 50: ";
    cin >> N;

    
    while (N < 1 || N > 50) {
        cout << "Numero no valido. Introduce un numero entre 1 y 50: ";
        cin >> N;
    }

    
    for (int i = 1; i <= N; i++) {
        cout << i << ") " << nombre << endl;
    }

    return 0;
}
