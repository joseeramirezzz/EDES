#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Clase Pokemon con atributos públicos
class Pokemon {
public:
    string nombre;
    string tipo;
    int nivel;
    int salud;

    // Constructor
    Pokemon(string n, string t, int l, int s) {
        nombre = n;
        tipo = t;
        nivel = l;
        salud = s;
    }

    // Mostrar información
    void mostrarInfo() {
        cout << "Nombre: " << nombre << endl;
        cout << "Tipo: " << tipo << endl;
        cout << "Nivel: " << nivel << endl;
        cout << "Salud: " << salud << endl;
        
    }

    // Curarse
    void curar(int puntos) {
        salud += puntos;
        cout << nombre << " se ha curado " << puntos << " puntos de salud!" << endl;
    }

    // Subir de nivel
    void subirNivel() {
        nivel++;
        cout << nombre << " ha subido al nivel " << nivel << "!" << endl;
    }
};

int main() {
    // Creamos un vector de Pokémon
    vector<Pokemon> equipo;
    equipo.push_back(Pokemon("Pikachu", "Eléctrico", 5, 50));
    equipo.push_back(Pokemon("Charmander", "Fuego", 4, 40));
    equipo.push_back(Pokemon("Bulbasaur", "Planta", 3, 45));

    // Mostramos información de todos los Pokémon
    cout << "Equipo Pokémon:" << endl;
    for (int i = 0; i < equipo.size(); i++) {
        equipo[i].mostrarInfo();
    }

    // Hacemos algunas acciones sobre ellos mismos
    equipo[0].curar(10);      // Pikachu se cura
    equipo[1].subirNivel();   // Charmander sube de nivel
    equipo[2].curar(5);       // Bulbasaur se cura

    // Mostramos información actualizada
    cout << "\nEstado actualizado del equipo:" << endl;
    for (int i = 0; i < equipo.size(); i++) {
        equipo[i].mostrarInfo();
    }

    return 0;
}
