import random
import matplotlib.pyplot as plt

# Número de estudiantes
total_students = 1000000

# Probabilidades
probability_woman = 400000 / total_students
probability_glasses = 300000 / total_students
probability_man_with_glasses = 150000 / total_students

# Función para generar una persona al azar con base en la transformada inversa
def generate_random_person():
    r1 = random.uniform(0, 1)  # Generamos un número aleatorio entre 0 y 1 para el género
    r2 = random.uniform(0, 1)  # Generamos otro número aleatorio entre 0 y 1 para los lentes
    
    if r1 <= probability_woman:
        gender = 'Mujer'
    else:
        gender = 'Varón'
    
    if r2 <= probability_glasses:
        glasses = 'Usa lentes'
    else:
        glasses = 'No usa lentes'
    
    return gender, glasses

# Simulación de "Probabilidad de ser mujer y usar gafas"
count_woman_and_glasses = 0
num_simulations = 10000  # Reducido para acelerar la simulación y el gráfico

# Lista para almacenar las probabilidades simuladas a lo largo de las simulaciones
simulated_probabilities_woman_and_glasses = []

for _ in range(num_simulations):
    gender, glasses = generate_random_person()
    if gender == 'Mujer' and glasses == 'Usa lentes':
        count_woman_and_glasses += 1
    
    # Calculamos la probabilidad simulada hasta el momento y la agregamos a la lista
    probability_so_far = count_woman_and_glasses / (_ + 1)
    simulated_probabilities_woman_and_glasses.append(probability_so_far)

# Simulación de "Probabilidad de ser varón dado que no usa lentes"
count_man_no_glasses = 0

# Lista para almacenar las probabilidades simuladas a lo largo de las simulaciones
simulated_probabilities_man_no_glasses = []

for _ in range(num_simulations):
    gender, glasses = generate_random_person()
    if gender == 'Varón' and glasses == 'No usa lentes':
        count_man_no_glasses += 1
    
    # Calculamos la probabilidad simulada hasta el momento y la agregamos a la lista
    probability_so_far = count_man_no_glasses / (_ + 1)
    simulated_probabilities_man_no_glasses.append(probability_so_far)

# Mostrar los resultados de las probabilidades calculadas en la consola
print(f"Probabilidad simulada de ser mujer y usar gafas: {simulated_probabilities_woman_and_glasses[-1]}")
print(f"Probabilidad simulada de ser varón dado que no usa lentes: {simulated_probabilities_man_no_glasses[-1]}")

# Crear gráficos
plt.figure(figsize=(12, 6))

# Gráfico para "Probabilidad de ser mujer y usar gafas"
plt.subplot(1, 2, 1)
plt.plot(range(1, num_simulations + 1), simulated_probabilities_woman_and_glasses, label='Simulado')
plt.axhline(y=probability_man_with_glasses, color='r', linestyle='--', label='Teórico')
plt.xlabel('Número de simulaciones')
plt.ylabel('Probabilidad')
plt.title('Probabilidad simulada de ser mujer y usar gafas')
plt.legend()

# Gráfico para "Probabilidad de ser varón dado que no usa lentes"
plt.subplot(1, 2, 2)
plt.plot(range(1, num_simulations + 1), simulated_probabilities_man_no_glasses, label='Simulado')
plt.axhline(y=0.6, color='r', linestyle='--', label='Teórico')  # Corrección aquí
plt.xlabel('Número de simulaciones')
plt.ylabel('Probabilidad')
plt.title('Probabilidad simulada de ser varón dado que no usa lentes')
plt.legend()

plt.tight_layout()
plt.show()
