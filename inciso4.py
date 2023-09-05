import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Parte A
p = 0.5
mu = 1/p
sigma_sq = (1-p)/p**2
sigma = np.sqrt(sigma_sq)

def generate_geometric(n, p):
    return np.random.geometric(p, n)

def simulate_discrete(n, N, mu, sigma):
    results = [(np.mean(generate_geometric(n, p)) - mu)/(sigma/np.sqrt(n)) for _ in range(N)]
    return results

# Paso 1 y 2
n = 20
N = 50
sim_results = simulate_discrete(n, N, mu, sigma)

# Paso 3
plt.hist(sim_results, bins='auto', density=True)
x = np.linspace(min(sim_results), max(sim_results), 100)
plt.plot(x, norm.pdf(x, 0, 1))
plt.show() 

# Paso 4
plt.hist(sim_results, bins='auto', density=True, cumulative=True, histtype='step')
x = np.linspace(min(sim_results), max(sim_results), 100)
plt.plot(x, norm.cdf(x, 0, 1))
plt.show()



#Parte B
lambda_val = 1.0
mu = 1/lambda_val
sigma_sq = 1/lambda_val**2
sigma = np.sqrt(sigma_sq)

def generate_exponential(n, lambda_val):
    return np.random.exponential(1/lambda_val, n)

def simulate_continuous(n, N, mu, sigma):
    results = [(np.mean(generate_exponential(n, lambda_val)) - mu)/(sigma/np.sqrt(n)) for _ in range(N)]
    return results

# Paso 1 y 2
n = 20
N = 50
sim_results = simulate_continuous(n, N, mu, sigma)

# Paso 3
plt.hist(sim_results, bins='auto', density=True)
x = np.linspace(min(sim_results), max(sim_results), 100)
plt.plot(x, norm.pdf(x, 0, 1))
plt.show()

# Paso 4
plt.hist(sim_results, bins='auto', density=True, cumulative=True, histtype='step')
x = np.linspace(min(sim_results), max(sim_results), 100)
plt.plot(x, norm.cdf(x, 0, 1))
plt.show()
