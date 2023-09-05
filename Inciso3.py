#El valor impreso será una estimación de la integral -xe-x2dx


import numpy as np

# Número de puntos aleatorios
N = 1000000

# Generar N números aleatorios uniformes en [0, 1]
random_numbers = np.random.uniform(0, 1, N)

# Función a integrar
def integrand(x):
    return -0.5 * x * np.exp(-x**2) + 0.5 * np.exp(-x**2)

# Estimar la integral usando el método de Montecarlo
integral_estimate = np.mean(integrand(random_numbers))

print("Estimación de la integral:", integral_estimate)
