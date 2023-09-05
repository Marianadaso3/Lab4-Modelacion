#Importaciones
import random
import matplotlib.pyplot as plt
import numpy as np

#Inciso A------------------------------------------------

# Función para generar valores de la distribución de Poisson con parámetro lambda
def generate_poisson(lambda_value):
    k = 0
    p = 1.0
    while True:
        k += 1
        p *= random.random()
        if p <= np.exp(-lambda_value):
            break
    return k

# Número de valores a generar
n = 100000

# Parámetro de la distribución de Poisson
lambda_value = 5

# Generar valores aleatorios y calcular las medias parciales
values = [generate_poisson(lambda_value) for _ in range(n)]
partial_means = [sum(values[:i+1]) / (i+1) for i in range(n)]

# Calcular la media real de la distribución de Poisson
real_mean = lambda_value

# Graficar las medias parciales y la media real
plt.plot(range(1, n+1), partial_means, label='Medias Parciales')
plt.axhline(y=real_mean, color='r', linestyle='--', label='Media Real')
plt.xlabel('n (Tamaño de la muestra)')
plt.ylabel('Media')
plt.title('Convergencia de Medias Parciales a la Media Real (Distribución de Poisson)')
plt.legend()
plt.show()


#Inciso B------------------------------------------------

# Función para generar valores de la distribución exponencial con parámetro lambda
def generate_exponential(lambda_value):
    return -np.log(1 - random.random()) / lambda_value

# Número de valores a generar
n = 10000

# Parámetro de la distribución exponencial
lambda_value = 2

# Generar valores aleatorios y calcular las medias parciales
values = [generate_exponential(lambda_value) for _ in range(n)]
partial_means = [sum(values[:i+1]) / (i+1) for i in range(n)]

# Calcular la media real de la distribución exponencial
real_mean = 1 / lambda_value

# Graficar las medias parciales y la media real
plt.plot(range(1, n+1), partial_means, label='Medias Parciales')
plt.axhline(y=real_mean, color='r', linestyle='--', label='Media Real')
plt.xlabel('n (Tamaño de la muestra)')
plt.ylabel('Media')
plt.title('Convergencia de Medias Parciales a la Media Real (Distribución Exponencial)')
plt.legend()
plt.show()
