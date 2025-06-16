# ZADANIE 1: Generowanie próby i analiza podstawowa
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parametr rozkładu wykładniczego (średnia, skala)
theta = 0.5
N = 1000

# Generujemy próbę losową z rozkładu wykładniczego
# W scipy.stats.expon.rvs parametr scale = theta
X = expon.rvs(scale=theta, size=N)

# Wyznaczamy statystyki z próby
srednia = np.mean(X)
wariancja = np.var(X, ddof=0)  # ddof=0 bo próbka, wzór zgodny z Var(X)
kurtosis = (np.mean((X - srednia)**4) / (np.var(X)**2)) - 3  # kurtoza zdefiniowana klasycznie

print("Srednia z próby:", srednia)
print("Wariancja z próby:", wariancja)
print("Kurtoza z próby:", kurtosis)
print("Wartość oczekiwana teoretyczna:", theta)
print("Wariancja teoretyczna:", theta**2)

# Rysujemy dystrybuantę empiryczną vs teoretyczna
sorted_X = np.sort(X)
empirical_cdf = np.arange(1, N + 1) / N

def F_teor(x):
    return 1 - np.exp(-x / theta)

plt.figure(figsize=(10, 6))
plt.step(sorted_X, empirical_cdf, label="Dystrybuanta empiryczna")
plt.plot(sorted_X, F_teor(sorted_X), label="Dystrybuanta teoretyczna", color='red')
plt.xlabel("x")
plt.ylabel("F(x)")
plt.legend()
plt.grid()
plt.title("Porównanie dystrybuanty empirycznej i teoretycznej")
plt.show()