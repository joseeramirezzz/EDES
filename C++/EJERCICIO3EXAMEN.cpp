#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Pokemon {
public:
    string nombrePokemon;
    int vida;
    double posiciona;
    double posicionb;
    string color;

    Pokemon(string nombre, int vida, double a, double b, string color) {
        nombrePokemon = nombre;
        vida = vida;
        posiciona = a;
        posicionb = b;
        color = color;
    }

    void gritar() {
        cout << "la motivacion y la constancia es la base del éxito" << endl;
    }

    void mover(double da, double db) {
        posiciona += da;
        posicionb += db;
    }

    void mostrarDatos() {
        cout << "Nombre: " << nombrePokemon << endl;
        cout << "Puntos de vida: " << vida << endl;
        cout << "Posicion a: " << posiciona << endl;
        cout << "Posicion b: " << posicionb << endl;
        cout << "Color: " << color << endl;
    }

    void jamacuco() {
        vida--;
        cout << nombrePokemon << " ha perdido una vida Vida restante: " << vida << endl;
    }
};

int main() {
    vector<Pokemon> listapokemon;

    listapokemon.push_back(Pokemon("Pikachu", 5, 0.0, 0.0, "amarillo"));
    listapokemon.push_back(Pokemon("Charmander", 4, 1.0, 1.0, "Rojo"));
    listapokemon.push_back(Pokemon("psyduck", 6, -2.0, 3.5, "verde"));
    listapokemon.push_back(Pokemon("Bulbasur", 8, 4.0, 4.0,"verde"));

    return 0;
}
