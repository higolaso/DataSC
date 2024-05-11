def verificar_solucion_ecuacion(x):
    # establecer las ecuaciones
    izquierda = (x - 5) ** 2
    derecha = (x + 1) ** 2
    # admitir que tal valor pueda ser solución igualando ambas ecuaciones
    if izquierda == derecha:
        print(f"{x} es una solución de la ecuación.")
    else:
        print(f"{x} no es una solución de la ecuación.")

# Verificar cuando x=2
verificar_solucion_ecuacion(2)

# Verificar cuando x=2
verificar_solucion_ecuacion(9)

# Verificar otro valor cualquiera x=5
verificar_solucion_ecuacion(12)
