# Importe de modulos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Definición de funciones f y g(x)
def f(x):
    return (x - 3)**2

def g(x):
    return 32 / (x - 3)**3

# Encontrar EL punto de intersección (5;4)
epsilon = 1e-6
a, b = 0, 10
dominio = np.arange(a, b, 0.01)
intersecciones = []
for x in dominio:
    if np.abs(f(x) - g(x)) < epsilon:
        intersecciones.append(x)

# Proyectar las funciones
fig, eje = plt.subplots()
eje.plot(dominio, f(dominio), label="f(x)")
eje.plot(dominio, g(dominio), label="g(x)")

# Y proyectar el punto de int.
for point in intersecciones:
    eje.plot(point, f(point), "ro")

# Detalles descriptivos
muestras_graficas = [Line2D([0], [0], color="red", lw=4),
                Line2D([0], [0], color="blue", lw=4),
                Line2D([0], [0], marker="o", color="red", label="Punto de intersección", markersize=10)]
eje.legend(muestras_graficas, ["f(x)", "g(x)", "Punto de intersección"])


# Límites y título del gráfico (En la hoja se detalla que es el único punto de int.)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
eje.set_title("f(x) y g(x). Punto de intersección en (5;4)")
eje.set_xlim(a, b)
eje.set_ylim(0, 100)
plt.show()
