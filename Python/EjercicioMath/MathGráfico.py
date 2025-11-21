import tkinter as tk
from tkinter import messagebox
import random
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generar():
    try:
        n = int(entry_cantidad.get())
        if n < 1000:
            messagebox.showerror("Error", "El número debe ser al menos 1000.")
            return
    except:
        messagebox.showerror("Error", "Introduce un número válido.")
        return

    # Generar números entre 0 y 1
    numeros = []
    for _ in range(n):
        numeros.append(random.random())

    # Calcular media
    media = sum(numeros) / n

    # Calcular varianza
    varianza = 0
    for x in numeros:
        varianza += (x - media) ** 2
    varianza /= n

    # Desviación estándar
    desviacion = math.sqrt(varianza)

    # Mostrar resultados
    label_media.config(text=f"Media: {media:.5f}")
    label_varianza.config(text=f"Varianza: {varianza:.5f}")
    label_desviacion.config(text=f"Desviación estándar: {desviacion:.5f}")

    # Graficar
    fig = Figure(figsize=(6, 3), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(numeros, label="Valores", linewidth=1)
    ax.axhline(media, color="red", linestyle="--", label="Media")
    ax.set_title("Gráfico de valores generados")
    ax.legend()

    # Mostrar gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10)
    canvas.draw()


# --- INTERFAZ TKINTER ---
window = tk.Tk()
window.title("Estadísticas con Tkinter y Gráficos")

tk.Label(window, text="Cantidad de números (mínimo 1000):").grid(row=0, column=0, pady=10)
entry_cantidad = tk.Entry(window)
entry_cantidad.grid(row=0, column=1)

btn = tk.Button(window, text="Generar y calcular", command=generar)
btn.grid(row=1, column=0, columnspan=2, pady=10)

label_media = tk.Label(window, text="Media: ")
label_media.grid(row=2, column=0, columnspan=2)

label_varianza = tk.Label(window, text="Varianza: ")
label_varianza.grid(row=3, column=0, columnspan=2)

label_desviacion = tk.Label(window, text="Desviación estándar: ")
label_desviacion.grid(row=4, column=0, columnspan=2)

window.mainloop()
