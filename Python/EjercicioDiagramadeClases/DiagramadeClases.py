class PlataformaNaval():

    def __init__ (self, nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad):
        
        self.nombre = nombre
        self.pais = pais
        self.eslora = eslora
        self.desplazamiento = desplazamiento
        self.velocidadMaxima = velocidadMaxima
        self.velocidadActual = velocidadActual
        self.rumboActual = rumboActual
        self.integridad = integridad

        self.sistemaArmas = sistemaArmas()
        self.sistemaSensores = sistemaSensores()

        self.Capitan = None

    def Navegar (self, nuevoRumbo, nuevaVelocidad):

        self.rumboActual = nuevoRumbo
        
        if nuevaVelocidad > self.velocidadMaxima:
            self.velocidadActual = self.velocidadMaxima
        else:
            self.velocidadActual = nuevaVelocidad

        print(f"El nuevo rumbo es {self.rumboActual} y la velocidad actual de {self.velocidadActual}")

    def detenerse (self):
        self.velocidadActual = 0
        print(f"La plataforma{self.nombre}, se ha detenido.")

    def recibirDaño (self,puntos):
        
        self.integridad = self.integridad - puntos

        if self.integridad < 0:
            self.integridad = 0
            print(f"Recibiste un daño de {puntos}, su integridad actual es 0.")
        else:
            print(f"Recibiste un daño de {puntos}, su integridad restante es de {self.integridad}")

    def estaOperativa (self):

        if self.integridad > 0:
            print(f"Operativa")
            return True
        else:
            print(f"No Operativa")
            return False


class Fragata(PlataformaNaval):
        def __init__(self, nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad, misilesAntiaereos, helicopterosEmb, rolPrincipal):
            super().__init__(nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad)
            self.misilesAntiaereos = misilesAntiaereos
            self.helicopterosEmb = helicopterosEmb
            self.rolPrincipal = rolPrincipal

        def dispararMisilAA(self):
            if self.misilesAntiaereos > 0:
                self.misilesAntiaereos = self.misilesAntiaereos - 1
                print(f"Se ha disparado un misil, dispones de {self.misilesAntiaereos}")
            else:
                print(f"Sin munición.")
        
        def despegarHelicoptero (self):
            if self.helicopterosEmb > 0:
                self.helicopterosEmb = self.helicopterosEmb - 1
                print (f"Quedan {self.helicopterosEmb} helicópteros a bordo.")
            else:
                print(f"No quedan Helicópteros a bordo.")


class Corbeta (PlataformaNaval):

    def __init__(self, nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad, misilesAntibuque, autonomiaDiasMax, automiaDiasRestante):
        super().__init__(nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad)
        self.misilesAntibuque = misilesAntibuque
        self.autonomiaDiasMax = autonomiaDiasMax
        self.automiaDiasRestante = automiaDiasRestante

    def dispararMisilAntibuque(self):
        if self.misilesAntibuque > 0:
            self.misilesAntibuque = self.misilesAntibuque - 1
            print(f"Has disparado un misil Antibuque. Te quedan {self.misilesAntibuque} misiles anti buque.")
        else:
            print(f"No te quedan misiles anti buque")

    def realizar_patrulla(self, costera: bool):
        if costera:
            print("Iniciando Patrulla costera.")
        else:
            print("Iniciando Patrulla de alta mar.")

        self.automiaDiasRestante = self.automiaDiasRestante - 1

        if self.automiaDiasRestante <= 0:
            self.automiaDiasRestante = 0
            print("La unidad necesita reabastecimiento.")
        else:
            print(f"Autonomía restante: {self.automiaDiasRestante} días.")


class Submarino (PlataformaNaval):

    def __init__(self, nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad, profundidadMaxima, tipoPropulsion, tubosLanzatorpedos, profundidadActual, enInmersion, torpedosDisponibles):
        super().__init__(nombre, pais, eslora, desplazamiento, velocidadMaxima, velocidadActual, rumboActual, integridad)
        self.profundidadMaxima = profundidadMaxima
        self.tipoPropulsion = tipoPropulsion
        self.tubosLanzatorpedos = tubosLanzatorpedos
        self.profundidadActual = profundidadActual
        self.enInmersion = enInmersion
        self.torpedosDisponibles = torpedosDisponibles

    def sumergirse(self, profundidad):
        if profundidad <= self.profundidadMaxima:
            self.profundidadActual = profundidad
            self.enInmersion = True
            print(f"Sumergido a {profundidad} metros.")
        else:
            print(f"Profundidad peligrosa, no se puede bajar.")

    def emerger(self):
        self.profundidadActual = 0
        self.enInmersion = False
        print("El submarino ha emergido.")

    def lanzarTorpedo(self):
        if self.torpedosDisponibles > 0:
            self.torpedosDisponibles = self.torpedosDisponibles - 1
            print(f"Torpedo lanzado. Torpedos restantes: {self.torpedosDisponibles}")
        else:
            print("No quedan torpedos disponibles.")


class sistemaArmas:

    def __init__(self, numCanones=0, numMisiles=0, numTorpedos=0):
        self.numCanones = numCanones
        self.numMisiles = numMisiles
        self.numTorpedos = numTorpedos
        self.objetivoActual = -1

    def seleccionarObjetivo(self, idObjetivo):
        self.objetivoActual = idObjetivo
        print(f"Objetivo seleccionado: {idObjetivo}")

    def dispararArma(self, tipo):
        if tipo == "canon":
            if self.numCanones > 0:
                self.numCanones -= 1
                print(f"Canon disparado. Restan {self.numCanones}")
            else:
                print("Sin munición de cañones")
        elif tipo == "misil":
            if self.numMisiles > 0:
                self.numMisiles -= 1
                print(f"Misil disparado. Restan {self.numMisiles}")
            else:
                print("Sin misiles")
        elif tipo == "torpedo":
            if self.numTorpedos > 0:
                self.numTorpedos -= 1
                print(f"Torpedo disparado. Restan {self.numTorpedos}")
            else:
                print("Sin torpedos")


class sistemaSensores:

    def __init__(self, tieneRadar=True, tieneSonar=True, rangoDeteccionKm=50):
        self.tieneRadar = tieneRadar
        self.tieneSonar = tieneSonar
        self.rangoDeteccionKm = rangoDeteccionKm
        self.ultimoContacto = "Ninguno"

    def escanearSuperficie(self):
        if self.tieneRadar:
            self.ultimoContacto = "Barco detectado en superficie"
            print("Barco detectado en superficie")
        else:
            print("No se puede escanear superficie")

    def escanearSubmarino(self):
        if self.tieneSonar:
            self.ultimoContacto = "Submarino detectado"
            print("Submarino detectado")
        else:
            print("No se puede detectar submarinos")


class Capitan:

    def __init__(self, nombre, rango, añosExperiencia):
        self.nombre = nombre
        self.rango = rango
        self.añosExperiencia = añosExperiencia
        self.plataformaActual = None

    def darOrden(self, orden):
        print(f"Capitán {self.nombre} ordena: {orden}")

    def asumirMando(self, plataforma):
        self.plataformaActual = plataforma
        plataforma.Capitan = self
        print(f"El capitán {self.nombre} ha asumido el mando de {plataforma.nombre}")


class Flota:

    def __init__(self, nombre, zonaOperacion):
        self.nombre = nombre
        self.zonaOperacion = zonaOperacion
        self.plataformas = []

    def agregarPlataforma(self, p):
        self.plataformas.append(p)
        print(f"{p.nombre} se ha unido a la flota {self.nombre}")

    def retirarPlataforma(self, p):
        if p in self.plataformas:
            self.plataformas.remove(p)
            print(f"{p.nombre} ha sido retirado de la flota {self.nombre}")

    def ordenarAtaque(self):
        print("Ataque coordinado iniciado.")
        for p in self.plataformas:
            if isinstance(p, Fragata):
                p.dispararMisilAA()
            elif isinstance(p, Corbeta):
                p.dispararMisilAntibuque()
            elif isinstance(p, Submarino):
                p.lanzarTorpedo()

# crear objetos

fragata_esp = Fragata(
    nombre="F-110 Numancia",
    pais="España",
    eslora=145,
    desplazamiento=6100,
    velocidadMaxima=28,
    velocidadActual=0,
    rumboActual=0,
    integridad=100,
    misilesAntiaereos=16,
    helicopterosEmb=1,
    rolPrincipal="Defensa aérea"
)


corbeta_esp = Corbeta(
    nombre="Descubierta",
    pais="España",
    eslora=88,
    desplazamiento=1500,
    velocidadMaxima=25,
    velocidadActual=0,
    rumboActual=0,
    integridad=100,
    misilesAntibuque=8,
    autonomiaDiasMax=15,
    automiaDiasRestante=15
)


submarino_esp = Submarino(
    nombre="submarino 1",
    pais="España",
    eslora=81,
    desplazamiento=3000,
    velocidadMaxima=20,
    velocidadActual=0,
    rumboActual=0,
    integridad=100,
    profundidadMaxima=500,
    tipoPropulsion="AIP",
    tubosLanzatorpedos=6,
    profundidadActual=0,
    enInmersion=False,
    torpedosDisponibles=18
)


# CREAR CAPITÁN Y ASIGNARLO A LA FRAGATA


capitan1 = Capitan("Alejandro Torres", "Capitán de Fragata", 22)
capitan1.asumirMando(fragata_esp)


# CREAR FLOTA Y AGREGAR LAS TRES PLATAFORMAS


flota_espanola = Flota("Flota Española", "Mar Mediterráneo")
flota_espanola.agregarPlataforma(fragata_esp)
flota_espanola.agregarPlataforma(corbeta_esp)
flota_espanola.agregarPlataforma(submarino_esp)


# FUNCIÓN PARA IMPRIMIR INFORMACIÓN DETALLADA


def imprimir_info(plataforma):
    print(f"Nombre: {plataforma.nombre}")
    print(f"País: {plataforma.pais}")
    print(f"Eslora: {plataforma.eslora} m")
    print(f"Desplazamiento: {plataforma.desplazamiento} t")
    print(f"Velocidad actual: {plataforma.velocidadActual} nudos")
    print(f"Rumbo actual: {plataforma.rumboActual}°")
    print(f"Integridad: {plataforma.integridad}")

    # Capitán
    if plataforma.Capitan:
        print(f"Capitán: {plataforma.Capitan.nombre} ({plataforma.Capitan.rango})")
    else:
        print("Capitán: Ninguno")

    # Sensores
    sensores = plataforma.sistemaSensores
    print("\n--- Sensores ---")
    print(f"Tiene radar: {sensores.tieneRadar}")
    print(f"Tiene sonar: {sensores.tieneSonar}")
    print(f"Rango detección: {sensores.rangoDeteccionKm} km")
    print(f"Último contacto: {sensores.ultimoContacto}")

    # Armas
    armas = plataforma.sistemaArmas
    print("\n--- Sistema de Armas ---")
    print(f"Cañones: {armas.numCanones}")
    print(f"Misiles: {armas.numMisiles}")
    print(f"Torpedos: {armas.numTorpedos}")



# IMPRIMIR INFORMACIÓN INICIAL


print("\n=== INFORMACIÓN INICIAL DE LA FLOTA ===")
for p in flota_espanola.plataformas:
    imprimir_info(p)



# SIMULACIÓN DE ACCIONES


print("\n=== ACCIONES ===")

# Fragata
fragata_esp.dispararMisilAA()
fragata_esp.despegarHelicoptero()

# Corbeta
corbeta_esp.realizar_patrulla(costera=True)

# Submarino
submarino_esp.sumergirse(250)
submarino_esp.sistemaSensores.escanearSubmarino()
submarino_esp.lanzarTorpedo()


# DAÑO Y CAMBIOS EN SENSORES/ARMAS


print("\n=== DAÑO Y MODIFICACIONES ===")

corbeta_esp.recibirDaño(30)

# Modificar sensores
fragata_esp.sistemaSensores.tieneRadar = False
submarino_esp.sistemaSensores.rangoDeteccionKm = 80

# Modificar arsenal
fragata_esp.sistemaArmas.numMisiles = 4
submarino_esp.sistemaArmas.numTorpedos = 10



# INFORMACIÓN FINAL


print("\n=== INFORMACIÓN FINAL DE LA FLOTA ===")
for p in flota_espanola.plataformas:
    imprimir_info(p)


# Listado final de plataformas
print("\n===== LISTADO FINAL DE PLATAFORMAS =====")
for p in flota_espanola.plataformas:
    print(f"- {p.nombre} ({p.__class__.__name__})")


