# Dla rozkładu lognormalnego wyznacz wartość oczekiwaną, a następnie sprawdź, czy średnia arytmetyczna z próby jest nieobciążonym estymatorem parametru średniej. Wysymuluj próbę prostą z
# rozkładu lognormalnego i na podstawie Metody Monte Carlo sprawdź własności estymatora.

# 📦 Import bibliotek
import numpy as np                    # biblioteka do obliczeń numerycznych i statystycznych
import matplotlib.pyplot as plt       # biblioteka do tworzenia wykresów

# 🔧 Parametry wejściowe
mu = 1                                # parametr µ rozkładu normalnego (średnia)
sigma = 0.5                           # parametr σ rozkładu normalnego (odchylenie standardowe)
n = 1000                              # liczność jednej próby (ilość obserwacji w jednej symulacji)
num_trials = 10000                    # liczba prób w symulacji Monte Carlo

# 🧮 Teoretyczna wartość oczekiwana rozkładu lognormalnego:
# Wzór: E[Y] = exp(mu + sigma^2 / 2)
theoretical_mean = np.exp(mu + 0.5 * sigma**2)

# Wyświetlenie wartości oczekiwanej z definicji
print(f"Teoretyczna wartość oczekiwana: {theoretical_mean:.4f}")

# 🎲 Symulacja Monte Carlo
sample_means = []                    # lista do przechowywania średnich z prób

np.random.seed(42)                   # ustalenie ziarna losowości dla powtarzalności wyników

# Pętla powtarzana num_trials razy
for _ in range(num_trials):
    # Generujemy próbkę z rozkładu lognormalnego: Y ~ LogN(µ, σ)
    sample = np.random.lognormal(mean=mu, sigma=sigma, size=n)
    
    # Obliczamy średnią arytmetyczną z tej próbki
    sample_mean = np.mean(sample)
    
    # Dodajemy ją do listy
    sample_means.append(sample_mean)

# Konwersja na tablicę numpy do dalszych obliczeń
sample_means = np.array(sample_means)

# 🔍 Obliczenie średniej z uzyskanych estymatorów (empiryczna wartość oczekiwana)
empirical_mean_of_means = np.mean(sample_means)

# Obliczenie obciążenia estymatora (bias)
bias = empirical_mean_of_means - theoretical_mean

# 📋 Wyświetlenie wyników końcowych
print(f"Średnia z {num_trials} estymatorów: {empirical_mean_of_means:.4f}")
print(f"Bias (obciążenie estymatora): {bias:.6f}")

# 📊 Wykres: histogram średnich z prób
plt.figure(figsize=(10, 5))           # tworzymy wykres o rozmiarze 10x5 cali

# Histogram zagęszczenia (density=True normalizuje sumę do 1)
plt.hist(sample_means, bins=50, density=True, alpha=0.7,
         color='skyblue', edgecolor='k', label='Empiryczne średnie')

# Linia przerywana – teoretyczna wartość oczekiwana
plt.axvline(theoretical_mean, color='red', linestyle='--', linewidth=2,
            label='Teoretyczna wartość oczekiwana')

# Linia przerywana – empiryczna średnia z prób
plt.axvline(empirical_mean_of_means, color='green', linestyle='--', linewidth=2,
            label='Średnia z estymatorów')

# Opisy osi i tytuł wykresu
plt.title("Rozkład średnich arytmetycznych z prób (Monte Carlo)")
plt.xlabel("Średnia arytmetyczna")
plt.ylabel("Gęstość")

# Legenda i siatka pomocnicza
plt.legend()
plt.grid(True)

# Automatyczne rozmieszczenie elementów
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()
