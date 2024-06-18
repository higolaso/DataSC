import numpy as np
import matplotlib.pyplot as plt

# Definicion de la función f(x)
def f(x):
    return 2*x**3 + 3*x**2 - 108*x - 1

# Definicion las rectas tangentes
def tangente_4(x):
    return 12*x - 305

def tangente_menos5(x):
    return 12*x + 424

# Rango de gráfico (basado en eje x)
x = np.linspace(-10, 10, 400)
y = f(x)

# Puntos donde la tangente es paralela a L
tangente_x = [4, -5]
tangente_y = [f(4), f(-5)]

# Graficar:
# unción
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = 2x^3 + 3x^2 - 108x - 1')
# recta L
plt.plot(x, 12*x + 9, label='y = 12x + 9', linestyle='--')
# Las rectas tangentes
plt.plot(x, tangente_4(x), label='Tangente en x=4: y = 12x - 305', linestyle='--')
plt.plot(x, tangente_menos5(x), label='Tangente en x=-5: y = 12x + 424', linestyle='--')

# Marcar los puntos paralelos a la recta L
plt.scatter(tangente_x, tangente_y, color='red')

# Titulos y presentación
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfica de f(x), recta L y sus similares tangentes paralelas')
plt.legend()
plt.grid(True)
plt.show()
