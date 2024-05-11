# Importe de modulos
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función cuadrática
def f(x):
    return x**2 + 10*x - 1200

# Definición de la recta secante
def recta_secante(x1, x2):
    m = (f(x2) - f(x1)) / (x2 - x1)
    return lambda x: m * (x - x1) + f(x1)

# Evaluar en dos puntos x de la función
a = 9
b = 12

# Proyectar la función cuadrática
x = np.linspace(-15, 15, 100)
y = f(x)
plt.plot(x, y, label="f(x)")

# Proyectar la recta secante
secante = recta_secante(a, b)
x_secante = np.linspace(a, b, 100)
y_secante = secante(x_secante)
plt.plot(x_secante, y_secante, label="Recta secante")

# Títulos del gráfico
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title("Secante de f(x) para a = 9 y b = 12")
plt.legend()
plt.grid(True)
plt.show()
