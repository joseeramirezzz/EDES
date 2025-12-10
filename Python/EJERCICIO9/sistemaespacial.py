# ============================================================
#   1. CUERPOS CELESTES NATURALES
# ============================================================

class CuerpoCeleste:
    """Clase base para todos los cuerpos celestes naturales."""

    def __init__(self, nombre, tipo, sistema, masa, x, y, vx, vy):
        self.nombre = nombre
        self.tipo = tipo  # planeta, satélite, cometa...
        self.sistema = sistema
        self.masa = masa
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def avanzar_tiempo(self):
        """Actualiza la posición según velocidad."""
        self.x += self.vx
        self.y += self.vy

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) en {self.sistema}"


# -------- PLANETA --------

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, sistema, masa, x, y, vx, vy,
                 radio_medio, max_satelites, atmosfera_densa):
        super().__init__(nombre, "Planeta", sistema, masa, x, y, vx, vy)
        self.radio_medio = radio_medio
        self.max_satelites = max_satelites
        self.atmosfera_densa = atmosfera_densa


# -------- SATÉLITE NATURAL --------

class SateliteNatural(CuerpoCeleste):
    def __init__(self, nombre, sistema, masa, x, y, vx, vy,
                 cuerpo_orbita, distancia_media):
        super().__init__(nombre, "Satélite Natural", sistema, masa, x, y, vx, vy)
        self.cuerpo_orbita = cuerpo_orbita
        self.distancia_media = distancia_media


# -------- COMETA --------

class Cometa(CuerpoCeleste):
    def __init__(self, nombre, sistema, masa, x, y, vx, vy,
                 periodo_orbital, cola_visible):
        super().__init__(nombre, "Cometa", sistema, masa, x, y, vx, vy)
        self.periodo_orbital = periodo_orbital
        self.cola_visible = cola_visible


# ============================================================
#   2. ESTRUCTURAS ESPACIALES HUMANAS
# ============================================================

class EstructuraEspacial:
    """Clase base para estructuras espaciales creadas por humanos."""

    def __init__(self, nombre_mision, agencia, pais, x, y, vx, vy, estado):
        self.nombre_mision = nombre_mision
        self.agencia = agencia
        self.pais = pais
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.estado = estado  # En órbita, fuera de servicio...

    def avanzar_tiempo(self):
        self.x += self.vx
        self.y += self.vy


# -------- SATÉLITE ARTIFICIAL --------

class SateliteArtificial(EstructuraEspacial):
    def __init__(self, nombre_mision, agencia, pais, x, y, vx, vy, estado,
                 orbita_cuerpo, altura_orbita, funcion,
                 propulsor, comunicacion):
        super().__init__(nombre_mision, agencia, pais, x, y, vx, vy, estado)

        self.orbita_cuerpo = orbita_cuerpo
        self.altura_orbita = altura_orbita
        self.funcion = funcion

        # Sistemas internos → COMPOSICIÓN
        self.propulsion = propulsor
        self.comunicaciones = comunicacion


# -------- COHETE --------

class Cohete(EstructuraEspacial):
    def __init__(self, nombre_mision, agencia, pais, x, y, vx, vy, estado,
                 empuje_total, capacidad_carga, lanzamientos,
                 propulsor, comunicacion):
        super().__init__(nombre_mision, agencia, pais, x, y, vx, vy, estado)
        self.empuje_total = empuje_total
        self.capacidad_carga = capacidad_carga
        self.lanzamientos = lanzamientos

        # Sistemas internos
        self.propulsion = propulsor
        self.comunicaciones = comunicacion

    def realizar_lanzamiento(self):
        self.lanzamientos += 1
        print(f"{self.nombre_mision} ha realizado un lanzamiento.")


# ============================================================
#   3. SISTEMAS INTERNOS (COMPOSICIÓN)
# ============================================================

class SistemaPropulsion:
    def __init__(self, tipo, combustible, empuje_max):
        self.tipo = tipo
        self.combustible = combustible
        self.empuje_max = empuje_max

    def consumir(self, cantidad):
        if self.combustible <= 0:
            print("Sin combustible.")
            return False
        self.combustible = max(0, self.combustible - cantidad)
        return True

    def hay_combustible(self):
        return self.combustible > 0


class SistemaComunicaciones:
    def __init__(self, potencia, frecuencias, operativo=True):
        self.potencia = potencia
        self.frecuencias = frecuencias
        self.operativo = operativo

    def enviar_mensaje(self, msg):
        if not self.operativo:
            print("Sistema de comunicaciones averiado.")
            return
        print(f"Transmitiendo mensaje: {msg}")


# ============================================================
#   4. AGRUPACIONES (AGREGACIÓN)
# ============================================================

class SistemaPlanetario:
    """Agrupa cuerpos celestes, pero NO los crea (AGREGACIÓN)."""

    def __init__(self, nombre, estrella):
        self.nombre = nombre
        self.estrella = estrella
        self.cuerpos = []  # planetas, satélites, cometas...

    def agregar_cuerpo(self, c):
        self.cuerpos.append(c)

    def listar(self):
        print(f"=== {self.nombre} (Estrella: {self.estrella}) ===")
        for c in self.cuerpos:
            print(f" - {c.nombre} ({c.tipo})")


class ConstelacionSat:
    def __init__(self, nombre, tipo_orbita):
        self.nombre = nombre
        self.tipo_orbita = tipo_orbita
        self.satelites = []  # estructuras espaciales

    def agregar(self, s):
        self.satelites.append(s)

        

# ============================================================
#   5. ASOCIACIÓN: CENTRO DE CONTROL
# ============================================================

class CentroControl:
    def __init__(self, nombre, pais, operadores):
        self.nombre = nombre
        self.pais = pais
        self.operadores = operadores
        self.misiones = []  # Puede controlar muchas misiones

    def asignar_mision(self, estructura):
        self.misiones.append(estructura)
        estructura.centro_control = self

    def enviar_orden(self, estructura, orden):
        print(f"[{self.nombre}] Orden enviada a {estructura.nombre_mision}: {orden}")

    def consultar_estado(self, estructura):
        print(f"{estructura.nombre_mision}: {estructura.estado}")
