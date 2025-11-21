import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import math
import random


# ---------------------------------------------------------
#                   CLASES DEL EJERCICIO ANTERIOR
# ---------------------------------------------------------

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
            f"--- Caja {self.codigo} ---\n"
            f"Peso: {self.peso_kg} kg\n"
            f"Descripción: {self.descripcion_carga}\n"
            f"Dimensiones: {self.largo}x{self.ancho}x{self.altura}\n"
        )


class Camion:
    def __init__(self, matricula, conductor, capacidad_kg, descripcion_carga, rumbo, velocidad):

        # datos
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []

        # posición inicial aleatoria
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 450)

        # tamaño visual del camión
        self.w = 50
        self.h = 30

        # color aleatorio
        self.color = random.choice(["red", "blue", "green", "orange", "purple", "yellow"])

    def peso_total(self):
        return sum(c.peso_kg for c in self.cajas)

    def add_caja(self, caja):
        if self.peso_total() + caja.peso_kg <= self.capacidad_kg:
            self.cajas.append(caja)
        else:
            raise ValueError("La caja excede la capacidad del camión")

    def setVelocidad(self, v):
        self.velocidad = v

    def setRumbo(self, r):
        if 1 <= r <= 359:
            self.rumbo = r
        else:
            raise ValueError("El rumbo debe estar entre 1 y 359")

    def __str__(self):
        info = (
            f"\n====== CAMIÓN {self.matricula} ======\n"
            f"Conductor: {self.conductor}\n"
            f"Capacidad: {self.capacidad_kg} kg\n"
            f"Descripción: {self.descripcion_carga}\n"
            f"Rumbo: {self.rumbo}\n"
            f"Velocidad: {self.velocidad}\n"
            f"Peso total: {self.peso_total()}\n"
            f"Cajas: {len(self.cajas)}\n"
        )
        for c in self.cajas:
            info += str(c)
        return info


# ---------------------------------------------------------
#                   INICIALIZAR PYGAME (CLAXON)
# ---------------------------------------------------------

# 1. Inicialización completa de Pygame (incluye todos los módulos)
pygame.init() 
# 2. Inicialización explícita del mezclador
pygame.mixer.init() 

# Variable global para almacenar el objeto Sound del claxon
claxon_sound = None 

def cargar_claxon():
    """
    Intenta cargar el archivo de sonido 'claxon.mp3' en la variable global.
    Utiliza pygame.mixer.Sound para mayor fiabilidad en efectos cortos.
    """
    global claxon_sound
    try:
        # Usamos Sound en lugar de music para efectos de sonido
        claxon_sound = pygame.mixer.Sound("claxon.mp3") 
        print("INFO: Archivo claxon.mp3 cargado con éxito.")
    except pygame.error as e:
        # Capturamos el error específico de Pygame si no encuentra el archivo
        # o hay un problema de formato.
        messagebox.showerror(
            "Error de Carga", 
            f"No se pudo cargar el archivo claxon.mp3.\nPor favor, verifica que está en la misma carpeta.\nError técnico: {e}"
        )
        print(f"ERROR: No se pudo cargar claxon.mp3: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado al cargar el claxon: {e}")


def tocar_claxon():
    """Reproduce el claxon usando el objeto Sound precargado."""
    global claxon_sound
    if claxon_sound:
        # .play() reproduce el sonido
        claxon_sound.play()
    else:
        # Si la carga inicial falló, se avisa al usuario
        messagebox.showerror("Error", "El claxon no está disponible porque el archivo no se pudo cargar al inicio.")


# Llama a la función de carga una vez al inicio del programa
cargar_claxon()


# ---------------------------------------------------------
#                   INTERFAZ TKINTER
# ---------------------------------------------------------

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Camiones SUPER GUAY")
        self.root.geometry("1100x650")

        self.camiones = []
        self.camion_activo = None

        # ---------- CANVAS ----------
        self.canvas = tk.Canvas(root, width=800, height=600, bg="#222")
        self.canvas.grid(row=0, column=0, rowspan=10)

        # ---------- PANEL ----------
        self.panel = tk.Frame(root)
        self.panel.grid(row=0, column=1, sticky="n")

        ttk.Label(self.panel, text="Camión activo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_camiones = ttk.Combobox(self.panel, state="readonly", width=15)
        self.combo_camiones.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        self.combo_camiones.bind("<<ComboboxSelected>>", self.cambiar_camion)

        # velocidad
        ttk.Label(self.panel, text="Velocidad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.vel_input = ttk.Entry(self.panel, width=10)
        self.vel_input.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Button(self.panel, text="Cambiar velocidad", command=self.cambiar_velocidad).grid(row=1, column=2, padx=5, pady=5)

        # rumbo
        ttk.Label(self.panel, text="Rumbo (1-359):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.rumbo_input = ttk.Entry(self.panel, width=10)
        self.rumbo_input.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Button(self.panel, text="Cambiar rumbo", command=self.cambiar_rumbo).grid(row=2, column=2, padx=5, pady=5)

        # añadir caja
        ttk.Button(self.panel, text="Añadir caja", command=self.crear_caja).grid(row=3, column=1, columnspan=2, padx=5, pady=10, sticky="ew")

        # info
        ttk.Button(self.panel, text="Mostrar información", command=self.mostrar_info).grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # claxon
        ttk.Button(self.panel, text="Claxon 🎺", command=tocar_claxon).grid(row=5, column=1, columnspan=2, padx=5, pady=20, sticky="ew")

        # crear camión
        ttk.Button(self.panel, text="Crear nuevo camión +", command=self.ventana_crear_camion).grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Inicializar camiones de prueba
        self.inicializar_camiones_prueba()
        
        # animación
        self.animar()

    # -----------------------------------------------------
    #           MÉTODOS DE CREACIÓN Y CAMBIO
    # -----------------------------------------------------

    def inicializar_camiones_prueba(self):
        """Crea algunos camiones de prueba al inicio."""
        try:
            cam1 = Camion("ABC-123", "Juan Pérez", 5000.0, "Alimentos perecederos", 45, 10)
            cam2 = Camion("XYZ-987", "Maria Gómez", 10000.0, "Maquinaria pesada", 225, 5)
            self.camiones.extend([cam1, cam2])
            self.actualizar_combo()
            
            # Seleccionar el primer camión por defecto
            if self.camiones:
                self.combo_camiones.set(self.camiones[0].matricula)
                self.cambiar_camion(None) # Ejecuta el cambio manualmente

        except Exception as e:
             # Este bloque no debería ejecutarse, pero es una buena práctica
             messagebox.showerror("Error de Inicio", f"Error al crear camiones de prueba: {e}")


    def ventana_crear_camion(self):
        win = tk.Toplevel(self.root)
        win.title("Nuevo camión")

        campos = ["Matrícula", "Conductor", "Capacidad (kg)", "Descripción",
                  "Rumbo", "Velocidad"]
        entradas = {}

        for i, campo in enumerate(campos):
            ttk.Label(win, text=campo + ":").grid(row=i, column=0, padx=5, pady=2, sticky="w")
            entradas[campo] = ttk.Entry(win)
            entradas[campo].grid(row=i, column=1, padx=5, pady=2, sticky="ew")

        def crear():
            try:
                cam = Camion(
                    entradas["Matrícula"].get(),
                    entradas["Conductor"].get(),
                    float(entradas["Capacidad (kg)"].get()),
                    entradas["Descripción"].get(),
                    int(entradas["Rumbo"].get()),
                    int(entradas["Velocidad"].get()),
                )

                self.camiones.append(cam)
                self.actualizar_combo()
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error de Entrada", str(e))

        ttk.Button(win, text="Crear", command=crear).grid(row=len(campos), column=0, columnspan=2, padx=5, pady=10)

    def crear_caja(self):
        if not self.camion_activo:
            messagebox.showinfo("Advertencia", "Debe seleccionar un camión activo primero.")
            return

        win = tk.Toplevel(self.root)
        win.title("Añadir Caja")

        campos = ["Código", "Peso", "Descripción", "Largo", "Ancho", "Alto"]
        entradas = {}

        for i, campo in enumerate(campos):
            ttk.Label(win, text=campo + ":").grid(row=i, column=0, padx=5, pady=2, sticky="w")
            entradas[campo] = ttk.Entry(win)
            entradas[campo].grid(row=i, column=1, padx=5, pady=2, sticky="ew")

        def crear():
            try:
                caja = Caja(
                    entradas["Código"].get(),
                    float(entradas["Peso"].get()),
                    entradas["Descripción"].get(),
                    float(entradas["Largo"].get()),
                    float(entradas["Ancho"].get()),
                    float(entradas["Alto"].get()),
                )
                self.camion_activo.add_caja(caja)
                messagebox.showinfo("Caja Añadida", f"Caja {caja.codigo} añadida al camión {self.camion_activo.matricula}.")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error de Carga", str(e))

        ttk.Button(win, text="Añadir", command=crear).grid(row=len(campos), column=0, columnspan=2, padx=5, pady=10)

    def actualizar_combo(self):
        self.combo_camiones["values"] = [c.matricula for c in self.camiones]

    def cambiar_camion(self, event):
        mat = self.combo_camiones.get()
        self.camion_activo = next((c for c in self.camiones if c.matricula == mat), None)
        if self.camion_activo:
             self.vel_input.delete(0, tk.END)
             self.vel_input.insert(0, str(self.camion_activo.velocidad))
             self.rumbo_input.delete(0, tk.END)
             self.rumbo_input.insert(0, str(self.camion_activo.rumbo))

    def cambiar_velocidad(self):
        if self.camion_activo:
            try:
                nueva_vel = int(self.vel_input.get())
                self.camion_activo.setVelocidad(nueva_vel)
                print(f"Velocidad de {self.camion_activo.matricula} cambiada a {nueva_vel}")
            except Exception as e:
                messagebox.showerror("Error", f"Velocidad inválida: {e}")

    def cambiar_rumbo(self):
        if self.camion_activo:
            try:
                nuevo_rumbo = int(self.rumbo_input.get())
                self.camion_activo.setRumbo(nuevo_rumbo)
                print(f"Rumbo de {self.camion_activo.matricula} cambiado a {nuevo_rumbo}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def mostrar_info(self):
        if self.camion_activo:
            # Crear una ventana de información con más detalle
            info_win = tk.Toplevel(self.root)
            info_win.title(f"Información: {self.camion_activo.matricula}")
            info_label = ttk.Label(info_win, text=str(self.camion_activo), justify=tk.LEFT, font=('Courier', 10))
            info_label.pack(padx=10, pady=10)
        else:
            messagebox.showinfo("Información", "No hay camión activo seleccionado.")

    # -----------------------------------------------------
    #                 ANIMACIÓN CON REBOTE
    # -----------------------------------------------------

    def animar(self):
        self.canvas.delete("all")

        for cam in self.camiones:
            
            # El factor 0.5 ajusta la velocidad para que no sea excesivamente rápido
            rad = math.radians(cam.rumbo)
            cam.x += math.cos(rad) * cam.velocidad * 0.5
            cam.y += math.sin(rad) * cam.velocidad * 0.5

            # REBOTE EN BORDES
            # Corrección de rebote para asegurar que el camión no se salga
            # Eje X
            if cam.x <= 0 or cam.x + cam.w >= 800:
                # Ajusta la posición para evitar que se quede atascado en el borde
                if cam.x <= 0: cam.x = 0 
                if cam.x + cam.w >= 800: cam.x = 800 - cam.w
                
                # Cambia el ángulo para reflejar
                cam.rumbo = (180 - cam.rumbo) % 360

            # Eje Y
            if cam.y <= 0 or cam.y + cam.h >= 600:
                # Ajusta la posición para evitar que se quede atascado en el borde
                if cam.y <= 0: cam.y = 0
                if cam.y + cam.h >= 600: cam.y = 600 - cam.h
                
                # Cambia el ángulo para reflejar
                cam.rumbo = (-cam.rumbo) % 360

            # dibujar camión
            self.canvas.create_rectangle(cam.x, cam.y, cam.x + cam.w, cam.y + cam.h,
                                         fill=cam.color, outline="white", width=2)

            # etiqueta
            self.canvas.create_text(cam.x + cam.w/2, cam.y - 10, text=cam.matricula,
                                     fill="white", font=("Arial", 10, "bold"))

            # resaltado del activo
            if self.camion_activo == cam:
                self.canvas.create_rectangle(cam.x-3, cam.y-3, cam.x+cam.w+3, cam.y+cam.h+3,
                                             outline="cyan", width=3)

        self.root.after(30, self.animar)


# ---------------------------------------------------------
#                 EJECUTAR PROGRAMA
# ---------------------------------------------------------

# Importante: Este bloque se mantiene al final para asegurar que todas las 
# inicializaciones y cargas de archivos (como el claxon) se hagan antes de 
# iniciar el bucle principal de Tkinter.

root = tk.Tk()
app = App(root)
root.mainloop()

# Para asegurar que Pygame se cierre limpiamente
pygame.quit()