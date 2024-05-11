# Importe de modulo
import numpy as np
import matplotlib.pyplot as plt

# Definicion de la función ReLU
def ReLU(x):
    return np.abs(x) + x / 2

# Definicion de las funciónes g y h(x)
def g(x):
    return ReLU(x + 1) - ReLU(x - 1) - 1

def h(x):
    return x

# Proyectar funciones
x = np.linspace(-5, 5, 400)
plt.plot(x, g(x), label="g(x)")
plt.plot(x, h(x), label="h(x)")

# Encontrar el conjunto de ceros de ReLU
C0 = x[ReLU(x) == 0]
print("conjunto de ceros de ReLU", C0)

# Encontrar el conjunto E donde g(x) == h(x))
E = x[np.isclose(g(x), h(x))]
print("Intersección de g(x) y h(x):", E)

# Proyectar conjuntos
plt.scatter(C0, np.zeros_like(C0), color='red', label='conjunto de ceros de ReLU')
plt.scatter(E, g(E), color='green', label='Intersección de g(x) y h(x)')

# Titulos del gráfico
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfica de g(x) y h(x), ceros e intersecciones')
plt.legend()
plt.grid(True)
plt.show()
