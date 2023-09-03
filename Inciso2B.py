#Este código generará una gráfica similar a la anterior, mostrando cómo las medias parciales se acercan a la media real a medida que n aumenta.

#Generamos los números aleatorios y calculamos las medias aritméticas parciales
import numpy as np
import matplotlib.pyplot as plt

# Parámetro de la distribución exponencial
lambda_param = 0.5

# Generar n=1,000,000 valores aleatorios
random_values = np.random.exponential(scale=1/lambda_param, size=1000000)

# Calcular medias aritméticas parciales
partial_means = np.cumsum(random_values) / np.arange(1, 1000001)

# Graficar las medias parciales
plt.plot(range(1, 1000001), partial_means)
plt.axhline(np.mean(random_values), color='red', linestyle='--', label='Media real')
plt.xlabel('n')
plt.ylabel('Media parcial')
plt.legend()
plt.show()
