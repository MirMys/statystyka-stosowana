# W wybranym środowisku napisz program do wyznaczania następujących statystyk dla danego wektora
# obserwacji: mediana, kwartyle, rozstęp z próby, rozstęp międzykwartylowy, wariancja z próby oraz
# odchylenie standardowe. Wyznacz wartości powyższych charakterystyk dla wysymulowanej próby z
# rozkładu normalnego z parametrami µ = 2 i σ = 2 o długości 2000 elementów. Otrzymane wyniki
# porównaj z wynikami uzyskanymi za pomocą funkcji wbudowanych.

import numpy as np

# 1. Symulacja próby z rozkładu normalnego N(μ=2, σ=2), n=2000
mu = 2
sigma = 2
n = 2000

sample = np.random.normal(loc=mu, scale=sigma, size=n)

# 2. Wyznaczenie statystyk "ręcznie" (bez wbudowanych funkcji)

# Sortowanie próby
sample_sorted = np.sort(sample)

# Mediana
if n % 2 == 1:
    median_manual = sample_sorted[n // 2]
else:
    median_manual = (sample_sorted[n // 2 - 1] + sample_sorted[n // 2]) / 2

# Kwartyle Q1 (25%) i Q3 (75%) - interpolacja metodą podstawową (pozycja: p*(n+1))
def percentile_manual(data, p):
    pos = p * (len(data) + 1) - 1
    if pos < 0:
        return data[0]
    if pos >= len(data) - 1:
        return data[-1]
    lower = int(np.floor(pos))
    upper = int(np.ceil(pos))
    frac = pos - lower
    return data[lower] * (1 - frac) + data[upper] * frac

q1_manual = percentile_manual(sample_sorted, 0.25)
q3_manual = percentile_manual(sample_sorted, 0.75)

# Rozstęp z próby
range_manual = sample_sorted[-1] - sample_sorted[0]

# Rozstęp międzykwartylowy (IQR)
iqr_manual = q3_manual - q1_manual

# Średnia próby
mean_manual = np.sum(sample) / n

# Wariancja z korektą Bessela (dzielenie przez n-1)
var_manual = np.sum((sample - mean_manual)**2) / (n - 1)

# Odchylenie standardowe
std_manual = np.sqrt(var_manual)

# 3. Statystyki z wbudowanych funkcji
median_builtin = np.median(sample)
q1_builtin = np.percentile(sample, 25)
q3_builtin = np.percentile(sample, 75)
range_builtin = np.ptp(sample)  # peak to peak = max - min
iqr_builtin = q3_builtin - q1_builtin
var_builtin = np.var(sample, ddof=1)  # ddof=1: korekta Bessela
std_builtin = np.std(sample, ddof=1)

# 4. Wyświetlenie wyników
print("Porównanie statystyk (ręczne vs wbudowane):\n")
print(f"Mediana: {median_manual:.5f} vs {median_builtin:.5f}")
print(f"Q1: {q1_manual:.5f} vs {q1_builtin:.5f}")
print(f"Q3: {q3_manual:.5f} vs {q3_builtin:.5f}")
print(f"Rozstęp: {range_manual:.5f} vs {range_builtin:.5f}")
print(f"Rozstęp międzykwartylowy (IQR): {iqr_manual:.5f} vs {iqr_builtin:.5f}")
print(f"Wariancja: {var_manual:.5f} vs {var_builtin:.5f}")
print(f"Odchylenie standardowe: {std_manual:.5f} vs {std_builtin:.5f}")
