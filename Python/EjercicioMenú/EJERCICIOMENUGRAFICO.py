import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime 
from PIL import Image, ImageTk 

HARMONY_BG_COLOR = "#333333"  
HARMONY_BTN_COLOR = "#555555"
HARMONY_FG_COLOR = "#F0F0F0" 
HARMONY_RED_COLOR = "#800000" 

IMAGE_FILE = "EjercicioMenú/rafaelalberti.png"


def conversion(a):
    return (a * 9/5 + 32)

def tabla(a):
    resultados = ""
    for i in range(11):
        resultado = i * a
        resultados += f"{a} x {i} = {resultado}\n"
    return resultados

def manejar_opcion_1_mod(root):
    try:
        celsius = simpledialog.askfloat("Conversión C to F", "Introduce la temperatura en Celsius:", parent=root)
        if celsius is not None:
            farenheit = conversion(celsius)
            messagebox.showinfo("Resultado de Conversión", f"La temperatura de {celsius}°C es igual a:\n{farenheit:.2f}°F")
    except Exception:
        messagebox.showerror("Error de Entrada", "Por favor, introduce un valor numérico válido.")

def manejar_opcion_2_mod(root):
    try:
        numero = simpledialog.askinteger("Tabla de Multiplicar", "Introduce el número para la tabla (hasta el 10):", parent=root)
        if numero is not None:
            resultados = tabla(numero)
            messagebox.showinfo(f"Tabla del {numero}", resultados)
    except Exception:
         messagebox.showerror("Error de Entrada", "Por favor, introduce un número entero.")

def salir_programa_mod(root):
    if messagebox.askyesno("Confirmación de Salida", "¿Estás seguro de que deseas cerrar el programa?"):
        root.quit()


class MenuApp:
    def __init__(self, master):
        self.master = master
        master.title("UTILIDADES ARMÓNICAS")
        master.geometry("400x300")
        master.minsize(350, 250)
        master.configure(bg=HARMONY_BG_COLOR)
        
        self.logo_image = None
        try:
            full_image = Image.open(IMAGE_FILE)
            logo_raw = full_image.resize((50, 50), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(logo_raw)
        except FileNotFoundError:
            print(f"AVISO: No se encontró el logo en {IMAGE_FILE}.") 
        except Exception:
            print("AVISO: Error al cargar/procesar el logo.")

        if self.logo_image:
            self.logo_label = tk.Label(
                master, 
                image=self.logo_image,
                bg=HARMONY_BG_COLOR
            )
            self.logo_label.place(relx=1.0, y=10, x=-10, anchor="ne") 

        self.menu_frame = tk.Frame(master, bg=HARMONY_BG_COLOR, bd=0, relief="flat")
        self.menu_frame.place(relx=0.5, rely=0.5, anchor="center") 

        self.crear_elementos_menu(self.menu_frame) 

        self.clock_label = tk.Label(
            master, 
            font=("Arial", 12, "bold"), 
            bg=HARMONY_BG_COLOR, 
            fg=HARMONY_FG_COLOR, 
            relief="flat", 
            bd=0
        )
        self.clock_label.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
        self.update_clock() 

    def crear_boton_minimalista(self, master, texto, comando, color_especial=False):
        fondo = HARMONY_RED_COLOR if color_especial else HARMONY_BTN_COLOR
        activo = HARMONY_BG_COLOR if color_especial else HARMONY_BTN_COLOR
        
        btn = tk.Button(
            master, 
            text=texto, 
            command=comando,
            font=("Arial", 10),
            width=30,
            bd=0, 
            relief="flat", 
            bg=fondo, 
            fg=HARMONY_FG_COLOR,
            activebackground=activo, 
            activeforeground=HARMONY_FG_COLOR
        )
        btn.pack(pady=5)
        return btn

    def crear_elementos_menu(self, master_frame):
        titulo = tk.Label(
            master_frame, 
            text="M E N Ú", 
            font=("Arial", 18, "bold"), 
            bg=HARMONY_BG_COLOR, 
            fg=HARMONY_FG_COLOR
        )
        titulo.pack(pady=(5, 15)) 

        self.crear_boton_minimalista(master_frame, "1. Conversión de Temperatura (C ⇄ F)", lambda: manejar_opcion_1_mod(self.master))
        self.crear_boton_minimalista(master_frame, "2. Tabla de Multiplicar (x10)", lambda: manejar_opcion_2_mod(self.master))
        self.crear_boton_minimalista(master_frame, "0. S A L I R", lambda: salir_programa_mod(self.master), color_especial=True)

    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.master.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()