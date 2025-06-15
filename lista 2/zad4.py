# Napisz program, w którym wygenerujesz próbkę o długości 1000 z rozkładu normalnego o średniej
# 10 i odchyleniu standardowym 5, a następnie na jej podstawie utwórz drugą próbkę poprzez dodanie
# 10 wartości odstających (na przykład z rozkładu jednostajnego na przedziale [50, 100]). Policz dla
# obu próbek średnią, medianę, rozstęp międzykwartylowy (IQR), wariancję, odchylenie standardowe,
# kurtozę oraz skośność. Porównaj otrzymane wartości. Narysuj histogramy oraz wykresy pudełkowe.
# Zinterpretuj wyniki.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

# 1. Wygenerowanie próbki z rozkładu normalnego N(10, 5)
np.random.seed(42)
mu = 10
sigma = 5
n = 1000
sample_normal = np.random.normal(mu, sigma, n)

# 2. Dodanie 10 wartości odstających z rozkładu jednostajnego [50, 100]
outliers = np.random.uniform(50, 100, 10)
sample_with_outliers = np.concatenate((sample_normal, outliers))

# 3. Funkcja do obliczania statystyk
def compute_statistics(data):
    stats = {
        'średnia': np.mean(data),
        'mediana': np.median(data),
        'IQR': np.percentile(data, 75) - np.percentile(data, 25),
        'wariancja': np.var(data, ddof=1),
        'odch.std.': np.std(data, ddof=1),
        'skośność': skew(data),
        'kurtoza': kurtosis(data)
    }
    return stats

# 4. Obliczenie statystyk dla obu próbek
stats_clean = compute_statistics(sample_normal)
stats_outliers = compute_statistics(sample_with_outliers)

# 5. Wyświetlenie porównania
print("Porównanie statystyk:\n")
for key in stats_clean:
    print(f"{key.capitalize():<15} | Bez odstających: {stats_clean[key]:>8.4f} | Z odstającymi: {stats_outliers[key]:>8.4f}")

# 6. Wizualizacja: histogramy
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.hist(sample_normal, bins=50, color='blue', alpha=0.7, label='Bez odstających')
plt.title('Histogram bez odstających')
plt.xlabel('Wartość')
plt.ylabel('Liczność')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(sample_with_outliers, bins=50, color='red', alpha=0.7, label='Z odstającymi')
plt.title('Histogram z odstającymi')
plt.xlabel('Wartość')
plt.ylabel('Liczność')
plt.legend()

plt.tight_layout()
plt.show()

# 7. Wizualizacja: wykresy pudełkowe
plt.figure(figsize=(8, 5))
plt.boxplot([sample_normal, sample_with_outliers], labels=['Bez odst.', 'Z odst.'], vert=False)
plt.title('Wykresy pudełkowe (boxplot)')
plt.xlabel('Wartości')
plt.grid(True)
plt.show()
