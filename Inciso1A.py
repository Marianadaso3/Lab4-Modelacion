import random

# Definimos la población total y las cantidades de mujeres y estudiantes que usan lentes
poblacion_total = 1000000
mujeres = 400000
lentes = 300000
varones_lentes = 150000

# Pregunta 1: Probabilidad de ser mujer y usar lentes
probabilidad_mujer_lentes = (mujeres / poblacion_total) * (varones_lentes / poblacion_total)

# Pregunta 2: Probabilidad de ser varón dado que no usa lentes
probabilidad_varon_sin_lentes = ((poblacion_total - lentes) / poblacion_total) * ((poblacion_total - varones_lentes) / poblacion_total)

print("Probabilidad de ser mujer y usar lentes:", probabilidad_mujer_lentes)
print("Probabilidad de ser varón sin usar lentes:", probabilidad_varon_sin_lentes)


import numpy as np
import matplotlib.pyplot as plt

# Parámetro de la distribución de Poisson
lambda_param = 3

# Número de valores aleatorios a generar
n = 1000000

# Generar n valores aleatorios de la distribución de Poisson
random_values = np.random.poisson(lambda_param, n)

# Calcular las medias aritméticas parciales
partial_means = np.cumsum(random_values) / np.arange(1, n + 1)

# Media real de la distribución
media_real = lambda_param

# Graficar las medias parciales
plt.plot(range(1, n + 1), partial_means)
plt.axhline(media_real, color='red', linestyle='--', label='Media real')
plt.xlabel('n')
plt.ylabel('Media parcial')
plt.legend()
plt.show()
