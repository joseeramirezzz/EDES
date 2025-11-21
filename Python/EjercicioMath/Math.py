import random
import math

n = int(input("¿Cuántos números quieres generar? (mínimo 1000): "))

while n < 1000:
    print("Debes introducir un número igual o mayor a 1000.")
    n = int(input("¿Cuántos números quieres generar? (mínimo 1000): "))


numeros = []
for i in range(n):
    numeros.append(random.random())


media = sum(numeros) / n


varianza = 0
for x in numeros:
    varianza += (x - media) ** 2
varianza = varianza / n



desviacion = math.sqrt(varianza)


print(f"\nCantidad de números generados: {n}")
print(f"Media: {media}")
print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desviacion}")
