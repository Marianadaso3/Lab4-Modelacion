import numpy as np
import matplotlib.pyplot as plt

# Parámetro de la distribución exponencial
lambda_param = 2

# Número de valores aleatorios a generar
n = 1000000

# Generar n valores aleatorios de la distribución exponencial
random_values = np.random.exponential(scale=1 / lambda_param, size=n)

# Calcular las medias aritméticas parciales
partial_means = np.cumsum(random_values) / np.arange(1, n + 1)

# Media real de la distribución
media_real = 1 / lambda_param

# Graficar las medias parciales
plt.plot(range(1, n + 1), partial_means)
plt.axhline(media_real, color='red', linestyle='--', label='Media real')
plt.xlabel('n')
plt.ylabel('Media parcial')
plt.legend()
plt.show()
