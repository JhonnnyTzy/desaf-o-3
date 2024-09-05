import numpy as np

# Definir la función f(x) = e^(-x)
def f(x):
    return np.exp(-x)

# Definir la derivada de f(x), f'(x) = -e^(-x)
def f_prime(x):
    return -np.exp(-x)

# Función para aproximar el valor de f(x) con derivadas de orden 1, 2 y 3
def aproximacion_orden_1(x0, x1):
    h = x1 - x0
    return f(x0) + f_prime(x0) * h

def aproximacion_orden_2(x0, x1):
    h = x1 - x0
    return f(x0) + f_prime(x0) * h + (h**2 / 2) * (-np.exp(-x0))  # Segunda derivada = e^(-x)

def aproximacion_orden_3(x0, x1):
    h = x1 - x0
    return (f(x0) + f_prime(x0) * h 
            + (h**2 / 2) * (-np.exp(-x0)) 
            + (h**3 / 6) * np.exp(-x0))  # Tercera derivada = -e^(-x)

# Función para calcular el error absoluto
def calcular_error(exacto, aproximado):
    return abs(exacto - aproximado)

# Cálculo del error total utilizando la propagación del error
def error_propagado(x0, x1, orden):
    # Valor exacto de f(x1)
    valor_real = f(x1)
    
    if orden == 1:
        aproximado = aproximacion_orden_1(x0, x1)
    elif orden == 2:
        aproximado = aproximacion_orden_2(x0, x1)
    elif orden == 3:
        aproximado = aproximacion_orden_3(x0, x1)
    else:
        raise ValueError("Orden no válido. Debe ser 1, 2 o 3.")
    
    # Cálculo del error absoluto
    error = calcular_error(valor_real, aproximado)
    return error

# Valores iniciales
x0 = 0.2
x1 = 1.0

# Cálculos de aproximaciones
resultado_orden_1 = aproximacion_orden_1(x0, x1)
resultado_orden_2 = aproximacion_orden_2(x0, x1)
resultado_orden_3 = aproximacion_orden_3(x0, x1)

# Cálculos de errores
error_orden_1 = error_propagado(x0, x1, 1)
error_orden_2 = error_propagado(x0, x1, 2)
error_orden_3 = error_propagado(x0, x1, 3)

# Mostrar resultados
print(f"Aproximación de orden 1: {resultado_orden_1} con error {error_orden_1}")
print(f"Aproximación de orden 2: {resultado_orden_2} con error {error_orden_2}")
print(f"Aproximación de orden 3: {resultado_orden_3} con error {error_orden_3}")
