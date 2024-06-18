import numpy as np
import matplotlib.pyplot as plt

# Definicion de la función f(x)
def f(x):
    return 1 / (-2*(x - 1)**2 + 16)

# Rango de gráfico (basado en eje x y las asintotas)
x = np.linspace(-2, 4, 400)
y = f(x)

# Graficar:
# La función
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$f(x) = \\frac{1}{-2(x-1)^2 + 16}$', color='blue')
# Los asintotas verticales
plt.axvline(x=1 + np.sqrt(8), color='orange', linestyle='--', label='Asíntotas verticales')
plt.axvline(x=1 - np.sqrt(8), color='orange', linestyle='--')
# La asintota horizontal
plt.axhline(y=0, color='green', linestyle='-', label='Asíntota horizontal')

# Marcar el extremo local
plt.scatter(1, f(1), color='red', label='Extremo local (1, f(1))')

# Titulos y presentación
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfica de f(x)')
plt.legend()
plt.grid(True)
plt.show()
