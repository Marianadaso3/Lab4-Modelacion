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
count_woman_and_glasses = 0 #contadores
num_simulations = 1000000  # Ajustar el número de simulaciones

for _ in range(num_simulations):
    # Generamos una persona aleatoria llamando a la función generate_random_person
    gender, glasses = generate_random_person()
    # Comprobamos si la persona generada es una mujer que usa gafas
    if gender == 'Mujer' and glasses == 'Usa lentes':
        # Si la persona cumple con la condición, incrementamos el contador
        count_woman_and_glasses += 1

# Calcular la probabilidad simulada
simulated_probability_woman_and_glasses = count_woman_and_glasses / num_simulations

print(f"Probabilidad simulada de ser mujer y usar gafas: {simulated_probability_woman_and_glasses}")

# Simulación de "Probabilidad de ser varón dado que no usa lentes"
count_man_no_glasses = 0 #contadores

for _ in range(num_simulations):
    gender, glasses = generate_random_person()
    if gender == 'Varón' and glasses == 'No usa lentes':
        count_man_no_glasses += 1

# Calcular la probabilidad simulada
simulated_probability_man_no_glasses = count_man_no_glasses / num_simulations
print(f"Probabilidad simulada de ser varón dado que no usa lentes: {simulated_probability_man_no_glasses}")

# Crear gráficos
plt.figure(figsize=(12, 6))

# Gráfico para "Probabilidad de ser mujer y usar gafas"
plt.subplot(1, 2, 1)
plt.plot(range(1, num_simulations + 1), [simulated_probability_woman_and_glasses] * num_simulations, label='Simulado')
plt.axhline(y=probability_man_with_glasses, color='r', linestyle='--', label='Teórico')
plt.xlabel('Número de simulaciones')
plt.ylabel('Probabilidad')
plt.title('Probabilidad simulada de ser mujer y usar gafas')
plt.legend()

# Gráfico para "Probabilidad de ser varón dado que no usa lentes"
plt.subplot(1, 2, 2)
plt.plot(range(1, num_simulations + 1), [simulated_probability_man_no_glasses] * num_simulations, label='Simulado')
plt.axhline(y=probability_man_with_glasses / (1 - probability_glasses), color='r', linestyle='--', label='Teórico')
plt.xlabel('Número de simulaciones')
plt.ylabel('Probabilidad')
plt.title('Probabilidad simulada de ser varón dado que no usa lentes')
plt.legend()

plt.tight_layout()
plt.show()
