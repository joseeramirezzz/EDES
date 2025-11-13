import tkinter as tk
from tkinter import ttk
import pygame
import math
from PIL import Image, ImageTk
import os
import random

# ---------------------------
# Clase Barco
# ---------------------------
class Barco:
    def __init__(self, nombre, x, y, velocidad, rumbo, municion, imagen_path):
        self.nombre = nombre
        self.x = float(x)
        self.y = float(y)
        self.velocidad = float(velocidad)
        self.rumbo = float(rumbo)
        self.municion = int(municion)
        self.imagen_original = Image.open(imagen_path).resize((60, 60))
        self.imagen_tk = ImageTk.PhotoImage(self.imagen_original)

    def mover(self, ancho, alto):
        rad = math.radians(self.rumbo)
        self.x += math.cos(rad) * self.velocidad * 0.5
        self.y -= math.sin(rad) * self.velocidad * 0.5

        # Rebote con los bordes
        if self.x <= 30 or self.x >= ancho - 30:
            self.rumbo = (180 - self.rumbo) % 360
        if self.y <= 30 or self.y >= alto - 30:
            self.rumbo = (-self.rumbo) % 360

    def disparar(self):
        if self.municion > 0:
            self.municion -= 1
            try:
                ruta_sonido = os.path.join(os.path.dirname(__file__), "sonido_disparo.mp3")
                pygame.mixer.Sound(ruta_sonido).play()
            except:
                print("⚠️ No se encontró el archivo de sonido del disparo.")
        else:
            print(f"⚠️ {self.nombre} sin munición.")

    def aumentar_velocidad(self):
        self.velocidad += 0.5

    def disminuir_velocidad(self):
        self.velocidad = max(0, self.velocidad - 0.5)

    def cambiar_rumbo_aleatorio(self):
        self.rumbo = random.randint(0, 359)

    def obtener_imagen_rotada(self):
        rotada = self.imagen_original.rotate(-self.rumbo, expand=True)
        return ImageTk.PhotoImage(rotada)


# ---------------------------
# Clase principal del simulador
# ---------------------------
class SimuladorBarcos:
    def __init__(self, root):
        self.root = root
        self.root.title("⚓ Simulador de Barcos - Interfaz Completa")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        # Inicializa pygame
        pygame.mixer.init()
        try:
            musica_path = os.path.join(os.path.dirname(__file__), "musica_fondo.mp3")
            pygame.mixer.music.load(musica_path)
            pygame.mixer.music.play(-1)
        except:
            print("⚠️ No se encontró 'musica_fondo.mp3'")

        self.barcos = []
        self.barco_activo = None

        # Fondo del mar
        fondo_path = os.path.join(os.path.dirname(__file__), "fondo.jpg")
        self.fondo_img = Image.open(fondo_path).resize((900, 700))
        self.fondo_tk = ImageTk.PhotoImage(self.fondo_img)

        # Canvas principal
        self.canvas = tk.Canvas(self.root, width=900, height=700, highlightthickness=0)
        self.canvas.pack(side="left")
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_tk)

        # Panel lateral
        self.panel = tk.Frame(self.root, bg="#1E2B3C", width=300)
        self.panel.pack(side="right", fill="y")

        tk.Label(self.panel, text="⚓ Control de Barcos", fg="white", bg="#1E2B3C",
                 font=("Segoe UI", 16, "bold")).pack(pady=15)

        # Entrada de nombre
        tk.Label(self.panel, text="Nombre del barco:", fg="white", bg="#1E2B3C").pack(pady=5)
        self.nombre_entry = ttk.Entry(self.panel, width=25)
        self.nombre_entry.pack(pady=5)

        ttk.Button(self.panel, text="➕ Crear barco", command=self.crear_barco).pack(pady=10)

        tk.Label(self.panel, text="Selecciona un barco:", fg="white", bg="#1E2B3C").pack(pady=5)
        self.selector = ttk.Combobox(self.panel, state="readonly")
        self.selector.pack(pady=5)
        self.selector.bind("<<ComboboxSelected>>", self.seleccionar_barco)

        # Botones de control
        ttk.Button(self.panel, text="🔫 Disparar", command=self.disparar).pack(pady=5)
        ttk.Button(self.panel, text="🧭 Cambiar rumbo automático", command=self.cambiar_rumbo_auto).pack(pady=5)
        ttk.Button(self.panel, text="⬆️ Aumentar velocidad", command=self.aumentar_velocidad).pack(pady=5)
        ttk.Button(self.panel, text="⬇️ Disminuir velocidad", command=self.disminuir_velocidad).pack(pady=5)

        self.info_label = tk.Label(self.panel, text="", fg="white", bg="#1E2B3C", justify="left", font=("Consolas", 10))
        self.info_label.pack(pady=20)

        # Bucle de actualización
        self.actualizar()

    # ---------------------------
    # Métodos funcionales
    # ---------------------------
    def crear_barco(self):
        nombre = self.nombre_entry.get().strip()
        if not nombre:
            return

        imagenes = ["barco.png", "barco2.jpg", "barco3.jpg"]
        imagen_path = os.path.join(os.path.dirname(__file__), random.choice(imagenes))

        x = random.randint(100, 800)
        y = random.randint(100, 600)
        velocidad = random.uniform(2, 4)
        rumbo = random.randint(0, 359)
        municion = random.randint(5, 15)

        nuevo = Barco(nombre, x, y, velocidad, rumbo, municion, imagen_path)
        self.barcos.append(nuevo)
        self.actualizar_selector()
        self.selector.set(nombre)
        self.barco_activo = nuevo
        self.nombre_entry.delete(0, tk.END)

    def actualizar_selector(self):
        self.selector["values"] = [b.nombre for b in self.barcos]

    def seleccionar_barco(self, event):
        nombre = self.selector.get()
        self.barco_activo = next((b for b in self.barcos if b.nombre == nombre), None)

    def disparar(self):
        if self.barco_activo:
            self.barco_activo.disparar()

    def aumentar_velocidad(self):
        if self.barco_activo:
            self.barco_activo.aumentar_velocidad()

    def disminuir_velocidad(self):
        if self.barco_activo:
            self.barco_activo.disminuir_velocidad()

    def cambiar_rumbo_auto(self):
        if self.barco_activo:
            self.barco_activo.cambiar_rumbo_aleatorio()

    # ---------------------------
    # Bucle de dibujo
    # ---------------------------
    def actualizar(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_tk)
        ancho, alto = 900, 700

        for b in self.barcos:
            b.mover(ancho, alto)
            img = b.obtener_imagen_rotada()
            b.imagen_tk = img
            self.canvas.create_image(b.x, b.y, image=img)
            self.canvas.create_text(b.x, b.y - 40, text=f"{b.nombre}", fill="white", font=("Segoe UI", 9, "bold"))

        # Actualiza panel de información
        if self.barco_activo:
            info = (f"Nombre: {self.barco_activo.nombre}\n"
                    f"Velocidad: {self.barco_activo.velocidad:.1f}\n"
                    f"Rumbo: {self.barco_activo.rumbo:.0f}°\n"
                    f"Munición: {self.barco_activo.municion}")
            self.info_label.config(text=info)
        else:
            self.info_label.config(text="Sin barco seleccionado")

        self.root.after(50, self.actualizar)


# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    estilo = ttk.Style()
    estilo.configure("TButton", font=("Segoe UI", 10), padding=6)
    app = SimuladorBarcos(root)
    root.mainloop()
