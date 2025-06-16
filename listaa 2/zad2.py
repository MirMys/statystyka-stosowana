# ZADANIE 2: Estymator i porównanie z rozkładem Gamma
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

M = 2000
theta = 0.5
N = 1000

# Tworzymy wektor estymatorów theta_1
estymatory = []
for _ in range(M):
    X = expon.rvs(scale=theta, size=N)
    theta_hat = np.mean(X)
    estymatory.append(theta_hat)

# Rysujemy boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(estymatory)
plt.title("Rozkład estymatora theta_1 (średnia próby)")
plt.grid()
plt.show()

# Porównanie dystrybuanty empirycznej z teoretyczną gamma
shape = N
scale = theta / N  # gamma z shape=N, scale=theta/N
sorted_est = np.sort(estymatory)
emp_cdf = np.arange(1, M + 1) / M
G_teor = gamma.cdf(sorted_est, a=shape, scale=scale)

plt.figure(figsize=(10, 6))
plt.step(sorted_est, emp_cdf, label="Empiryczna dystrybuanta estymatora")
plt.plot(sorted_est, G_teor, color='red', label="Teoretyczna gamma CDF")
plt.legend()
plt.grid()
plt.title("Porównanie dystrybuanty estymatora theta_1 z gamma")
plt.show()
