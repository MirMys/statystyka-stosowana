import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# ZADANIE 3: Wariancja estymatora vs długość próby
N_values = [10, 20, 100, 1000]
M = 1000

variances_theta1 = []
variances_theta2 = []

for N in N_values:
    t1, t2 = [], []
    for _ in range(M):
        X = expon.rvs(scale=2, size=N)  # theta = 2
        x_mean = np.mean(X)
        theta_1 = x_mean
        theta_2 = np.sqrt(np.sum((X - x_mean)**2) / (N - 1))
        t1.append(theta_1)
        t2.append(theta_2)

    variances_theta1.append(np.var(t1, ddof=1))
    variances_theta2.append(np.var(t2, ddof=1))

# Rysowanie wykresów wariancji estymatorów vs długość próby
plt.figure(figsize=(10, 6))
plt.plot(N_values, variances_theta1, label="Wariancja estymatora theta_1", marker='o')
plt.plot(N_values, variances_theta2, label="Wariancja estymatora theta_2", marker='s')
plt.xlabel("Długość próby N")
plt.ylabel("Wariancja estymatora")
plt.legend()
plt.grid()
plt.title("Porównanie wariancji estymatorów w zależności od długości próby")
plt.show()