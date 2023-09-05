import numpy as np

# Definimos la función que queremos integrar
def f(x):
    return x * np.exp(-x**2)

# Definimos la función g(x) que usaremos para el método de aceptación y rechazo
# Usaremos una distribución normal estándar, cuya pdf es (1/√(2π))e^(-x^2/2)
def g(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)

# Definimos la constante M que necesitamos para el método de aceptación y rechazo
# M es el máximo de f(x)/g(x), y necesitamos elegir un M tal que f(x)/g(x) <= M para todo x
# Para esta función, podemos elegir M = 1/√(2π), ya que f(x)/g(x) = x√(2π), y |x| <= 1/√(2π)
M = 1/np.sqrt(2*np.pi)

# Número de muestras que generaremos
N = 10000000

# Generamos muestras de una distribución normal estándar
x_samples = np.random.normal(0, 1, N)

# Calculamos los valores de f(x) y g(x) para estas muestras
f_values = f(x_samples)
g_values = g(x_samples)

# Usamos el método de aceptación y rechazo para generar muestras de f(x)
# Aceptamos una muestra x con probabilidad f(x)/(M*g(x))
accept = np.random.rand(N) < f_values / (M*g_values)

# Calculamos el valor estimado de la integral usando las muestras aceptadas
integral_estimate = np.mean(f_values[accept])

print(integral_estimate)

