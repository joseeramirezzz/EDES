class Caja:
    def __init__(self, codigo, peso_kg, descripcion_carga, largo, ancho, altura):
        self.codigo = codigo
        self.peso_kg = peso_kg
        self.descripcion_carga = descripcion_carga
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def __str__(self):
        return (
            f"\n   --- CAJA {self.codigo} ---"
            f"\n   Peso: {self.peso_kg} kg"
            f"\n   Descripción: {self.descripcion_carga}"
            f"\n   Dimensiones: {self.largo} x {self.ancho} x {self.altura}"
        )


class Camion:
    def __init__(self, matricula, conductor, capacidad_kg, descripcion_carga, rumbo, velocidad):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []

    def peso_total(self):
        return sum(caja.peso_kg for caja in self.cajas)

    def add_caja(self, caja):
        if self.peso_total() + caja.peso_kg <= self.capacidad_kg:
            self.cajas.append(caja)
        else:
            print(f"No se puede añadir la caja {caja.codigo}: excede la capacidad del camión.")

    def setVelocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad

    def setRumbo(self, nuevo_rumbo):
        self.rumbo = nuevo_rumbo

    def claxon(self):
        print("pitaaa")

    def __str__(self):
        info_cajas = "".join(str(caja) for caja in self.cajas)
        return (
            f"\n--- DATOS DEL CAMIÓN ---"
            f"\nMatrícula: {self.matricula}"
            f"\nConductor: {self.conductor}"
            f"\nCapacidad máxima: {self.capacidad_kg} kg"
            f"\nDescripción carga: {self.descripcion_carga}"
            f"\nRumbo: {self.rumbo}"
            f"\nVelocidad: {self.velocidad} km/h"
            f"\nNúmero de cajas: {len(self.cajas)}"
            f"\nPeso total: {self.peso_total()} kg"
            f"\n--- LISTA DE CAJAS ---"
            f"{info_cajas if info_cajas else '   (sin cajas)'}"
        )


c1 = Caja("C1", 100, "Ropa", 1.0, 0.5, 0.3)
c2 = Caja("C2", 150, "Electrónica", 1.2, 0.6, 0.4)
c3 = Caja("C3", 80, "Juguetes", 0.8, 0.4, 0.3)

c4 = Caja("C4", 200, "Herramientas", 1.5, 0.7, 0.5)
c5 = Caja("C5", 120, "Libros", 1.0, 0.5, 0.4)
c6 = Caja("C6", 90, "Utensilios", 0.9, 0.4, 0.3)



camion1 = Camion("1234-ABC", "Juan ", 700, "Carga", 120, 80)
camion2 = Camion("5678-XYZ", "María ", 900, "Material", 250, 95)


for caja in (c1, c2, c3):
    camion1.add_caja(caja)

for caja in (c4, c5, c6):
    camion2.add_caja(caja)


print("\n----- ANTES DE MODIFICAR NADA -----")
print(camion1)
print(camion2)


nueva1 = Caja("C7", 110, "Comida", 1.1, 0.5, 0.4)
nueva2 = Caja("C8", 150, "Líquidos", 1.3, 0.6, 0.5)

camion1.add_caja(nueva1)
camion1.add_caja(nueva2)

nueva3 = Caja("C9", 130, "Textiles", 1.0, 0.5, 0.5)
nueva4 = Caja("C10", 140, "Medicinas", 1.1, 0.4, 0.4)
nueva5 = Caja("C11", 200, "Piezas metálicas", 1.5, 0.7, 0.6)

camion2.add_caja(nueva3)
camion2.add_caja(nueva4)
camion2.add_caja(nueva5)


camion1.setVelocidad(95)
camion1.setRumbo(180)

camion2.setVelocidad(110)
camion2.setRumbo(300)

camion2.claxon()



print("\n--- DESPUÉS DE LOS CAMBIOS ---")
print(camion1)
print(camion2)
