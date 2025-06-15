# 5. Niech X będzie zmienną losową z rozkładu normalnego z parametrami µ i σ.
# a) Wyznacz gęstość zmiennej losowej Y = |X − E(X)| oraz wartość oczekiwaną E[Y ]. Zweryfikuj
# wyniki symulacyjnie.
# a) Wysymuluj próbę długości n z rozkładu N(µ, σ) dla przykładowych wielkości µ i σ. Porównaj
# teoretyczną wartość E(Y ) z empirycznym odpowiednikiem, tj. przeciętnym odchyleniem od średniej
# dla wysymulowanej próby. Wykonaj wykres zależności odległości tych dwóch wielkości w zależności
# od długości wysymulowanej próby

import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu
mu = 0
sigma = 2

# Teoretyczna wartość oczekiwana E[Y] = σ * sqrt(2 / π)
expected_Y_theoretical = sigma * np.sqrt(2 / np.pi)
print(f"Teoretyczna wartość E[Y]: {expected_Y_theoretical:.4f}")

# Funkcja do obliczania empirycznej wartości E[Y] dla próby
def empirical_E_Y(n, mu=mu, sigma=sigma):
    sample = np.random.normal(mu, sigma, n)
    Y = np.abs(sample - mu)
    return np.mean(Y)

# Porównanie dla jednej dużej próby
np.random.seed(42)
n_sample = 100_000
empirical_E = empirical_E_Y(n_sample)
print(f"Empiryczna wartość E[Y] (n={n_sample}): {empirical_E:.4f}")

# Wykres odchylenia empirycznej E[Y] od teoretycznej w zależności od n
sample_sizes = np.arange(10, 5001, 50)
deviations = []

for n in sample_sizes:
    est = empirical_E_Y(n)
    deviation = abs(est - expected_Y_theoretical)
    deviations.append(deviation)

# Wykres zależności odległości od wartości teoretycznej
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, deviations, label='|Empiryczne E[Y] - Teoretyczne E[Y]|', color='green')
plt.axhline(0, color='black', linestyle='--', alpha=0.6)
plt.xlabel("Rozmiar próby (n)")
plt.ylabel("Różnica bezwzględna")
plt.title("Zbieżność empirycznego E[Y] do teoretycznego")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
