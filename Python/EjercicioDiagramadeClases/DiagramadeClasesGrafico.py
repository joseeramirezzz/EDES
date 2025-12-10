import tkinter as tk
from tkinter import ttk, messagebox

# Importamos tus clases:
from DiagramadeClases import Fragata, Corbeta, Submarino, Flota


# ============================================================
# CONFIGURACIÓN INICIAL – CREAMOS LAS PLATAFORMAS Y LA FLOTA
# ============================================================

fragata = Fragata("F-110 Numancia", "España", 145, 6100, 28, 0, 0, 100, 16, 1, "Defensa aérea")
corbeta = Corbeta("Descubierta", "España", 88, 1500, 25, 0, 0, 100, 8, 15, 15)
submarino = Submarino("S-81 Isaac Peral", "España", 81, 3000, 20, 0, 0, 100, 500, "AIP", 6, 0, False, 18)

flota = Flota("Flota Española", "Mediterráneo")
flota.agregarPlataforma(fragata)
flota.agregarPlataforma(corbeta)
flota.agregarPlataforma(submarino)


# ============================================================
# CLASE PRINCIPAL DE LA INTERFAZ
# ============================================================

class InterfazFlota:

    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Naval")

        # -----------------------
        # Canvas principal
        # -----------------------
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.grid(row=0, column=0)

        # Posiciones iniciales
        self.pos = {
            fragata: [100, 100],
            corbeta: [200, 300],
            submarino: [400, 200]
        }

        # Dibujos en canvas
        self.iconos = {
            fragata: self.canvas.create_rectangle(80, 80, 140, 120, fill="gray", outline="black"),
            corbeta: self.canvas.create_rectangle(180, 280, 240, 320, fill="green", outline="black"),
            submarino: self.canvas.create_oval(380, 180, 420, 220, fill="darkblue", outline="black")
        }

        # -----------------------
        # Panel lateral
        # -----------------------
        self.panel = tk.Frame(root, width=300, height=600, bg="white")
        self.panel.grid(row=0, column=1, sticky="ns")

        self.titulo = tk.Label(self.panel, text="Información", font=("Arial", 14, "bold"))
        self.titulo.pack(pady=10)

        self.info_text = tk.Text(self.panel, width=35, height=20)
        self.info_text.pack()

        self.boton_estado_flota = tk.Button(self.panel, text="Estado de la Flota", command=self.mostrar_estado_flota)
        self.boton_estado_flota.pack(pady=5)

        # Botones acción
        tk.Button(self.panel, text="Mover Fragata", command=lambda: self.mover_plataforma(fragata, 20, 0)).pack()
        tk.Button(self.panel, text="Mover Corbeta", command=lambda: self.mover_plataforma(corbeta, -20, 0)).pack()
        tk.Button(self.panel, text="Mover Submarino", command=lambda: self.mover_plataforma(submarino, 0, 20)).pack()

        tk.Button(self.panel, text="Escanear Sensores", command=self.escanear_sensores).pack(pady=5)
        tk.Button(self.panel, text="Lanzar Arma", command=self.lanzar_arma).pack(pady=5)
        tk.Button(self.panel, text="Simular Daño", command=self.simular_daño).pack(pady=5)
        tk.Button(self.panel, text="Ataque Coordinado", command=self.ataque_coordinado).pack(pady=5)

        # Actualiza panel cuando se seleccione barco
        self.canvas.bind("<Button-1>", self.mostrar_info_click)

        self.actualizar_panel(fragata)

    # ============================================================
    # FUNCIONES DE INTERACCIÓN
    # ============================================================

    def actualizar_panel(self, p):
        """Muestra información de una plataforma en el panel."""
        self.info_text.delete("1.0", tk.END)

        estado = "OK" if p.integridad > 70 else "Dañado" if p.integridad > 0 else "Hundido"

        texto = (
            f"Nombre: {p.nombre}\n"
            f"País: {p.pais}\n"
            f"Eslora: {p.eslora} m\n"
            f"Integridad: {p.integridad} ({estado})\n\n"
            f"--- Armamento ---\n"
            f"Cañones: {p.sistemaArmas.numCanones}\n"
            f"Misiles: {p.sistemaArmas.numMisiles}\n"
            f"Torpedos: {p.sistemaArmas.numTorpedos}\n\n"
            f"--- Sensores ---\n"
            f"Radar: {p.sistemaSensores.tieneRadar}\n"
            f"Sonar: {p.sistemaSensores.tieneSonar}\n"
            f"Rango: {p.sistemaSensores.rangoDeteccionKm} km\n"
            f"Último contacto: {p.sistemaSensores.ultimoContacto}\n"
        )

        self.info_text.insert(tk.END, texto)

    def mostrar_info_click(self, event):
        """Detecta si se ha hecho clic sobre un barco."""
        x, y = event.x, event.y
        seleccionados = self.canvas.find_overlapping(x, y, x, y)

        for obj in seleccionados:
            for plataforma, icono in self.iconos.items():
                if icono == obj:
                    self.actualizar_panel(plataforma)

    # ============================================================
    # MOVIMIENTO
    # ============================================================

    def mover_plataforma(self, p, dx, dy):
        icono = self.iconos[p]
        self.canvas.move(icono, dx, dy)
        self.pos[p][0] += dx
        self.pos[p][1] += dy

        self.detectar_proximidad()
        self.actualizar_panel(p)

    # ============================================================
    # SENSORES
    # ============================================================

    def escanear_sensores(self):
        """Activa sensores y detecta enemigos si están cerca."""
        for p in flota.plataformas:
            for otro in flota.plataformas:
                if p == otro:
                    continue

                x1, y1 = self.pos[p]
                x2, y2 = self.pos[otro]

                distancia = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

                if distancia < 150:
                    p.sistemaSensores.ultimoContacto = f"Contacto detectado: {otro.nombre}"

        self.actualizar_panel(fragata)  # refresco arbitrario

    def detectar_proximidad(self):
        """Se llama tras cada movimiento."""
        self.escanear_sensores()

    # ============================================================
    # ARMAS
    # ============================================================

    def lanzar_arma(self):
        """El usuario elige quién dispara y contra quién."""
        window = tk.Toplevel(self.root)
        window.title("Lanzar arma")

        tk.Label(window, text="Atacante:").pack()
        atacante_cb = ttk.Combobox(window, values=[p.nombre for p in flota.plataformas])
        atacante_cb.pack()

        tk.Label(window, text="Objetivo:").pack()
        objetivo_cb = ttk.Combobox(window, values=[p.nombre for p in flota.plataformas])
        objetivo_cb.pack()

        def ejecutar():
            atacante = next(p for p in flota.plataformas if p.nombre == atacante_cb.get())
            objetivo = next(p for p in flota.plataformas if p.nombre == objetivo_cb.get())

            if atacante == objetivo:
                messagebox.showerror("Error", "No puedes atacar a tu propia plataforma")
                return

            # animación simple
            self.animacion_proyectil(atacante, objetivo)

            # daño básico
            objetivo.recibirDaño(20)

            self.actualizar_panel(objetivo)

        tk.Button(window, text="Disparar", command=ejecutar).pack(pady=10)

    def animacion_proyectil(self, atacante, objetivo):
        """Dibuja una línea en movimiento entre dos plataformas."""
        x1, y1 = self.pos[atacante]
        x2, y2 = self.pos[objetivo]

        linea = self.canvas.create_line(x1, y1, x1, y1, fill="red", width=2)

        pasos = 20
        for i in range(1, pasos + 1):
            nx = x1 + (x2 - x1) * i / pasos
            ny = y1 + (y2 - y1) * i / pasos
            self.canvas.coords(linea, x1, y1, nx, ny)
            self.canvas.update()
            self.canvas.after(20)

        self.canvas.delete(linea)

    # ============================================================
    # DAÑO
    # ============================================================

    def simular_daño(self):
        """Aplica daño aleatorio a la fragata."""
        fragata.recibirDaño(15)
        self.actualizar_panel(fragata)

    # ============================================================
    # ESTADO DE LA FLOTA
    # ============================================================

    def mostrar_estado_flota(self):
        texto = "=== ESTADO DE LA FLOTA ===\n\n"
        for p in flota.plataformas:
            estado = "OK" if p.integridad > 70 else "Dañado" if p.integridad > 0 else "Hundido"
            texto += f"{p.nombre} ({p.__class__.__name__}): {estado}\n"

        messagebox.showinfo("Estado de la Flota", texto)

    # ============================================================
    # ATAQUE COORDINADO
    # ============================================================

    def ataque_coordinado(self):
        flota.ordenarAtaque()
        messagebox.showinfo("Ataque", "La flota ha ejecutado un ataque coordinado.")


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFlota(root)
    root.mainloop()
