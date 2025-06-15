#  Wysymuluj próbę z rozkładu normalnego o długości n z parametrami µ = 2.1 oraz σ = 0.2. Wyznacz
# przedział ufności dla µ dla α = 0.02. Powtórz te procedurę 1000 razy i sprawdź ile razy teoretyczna
# wartość µ wpada w wyznaczony przedział ufności. Wyniki sprawdź dla n = 20, 50 oraz n = 100.
# Rozpatrz przypadki, gdy σ jest znana i nieznana.

# 📦 Import bibliotek
import numpy as np
from scipy.stats import norm, t
import matplotlib.pyplot as plt

# 📌 Parametry rozkładu normalnego
mu = 2.1          # średnia rozkładu
sigma = 0.2       # znane odchylenie standardowe (dla pierwszego przypadku)
alpha = 0.02      # poziom istotności -> poziom ufności = 98%
confidence = 1 - alpha
n_trials = 1000   # liczba powtórzeń symulacji

# 📊 Rozmiary próby do przetestowania
sample_sizes = [20, 50, 100]

# 🔁 Przejście po różnych rozmiarach próby
for n in sample_sizes:
    # Zliczacze trafień w przedział
    known_sigma_hits = 0
    unknown_sigma_hits = 0

    # 🔁 Powtarzamy eksperyment n_trials razy
    for _ in range(n_trials):
        # 🔢 Wygeneruj próbę długości n z rozkładu N(μ=2.1, σ=0.2)
        sample = np.random.normal(loc=mu, scale=sigma, size=n)

        # 🔹 Oblicz statystyki z próby
        sample_mean = np.mean(sample)            # średnia próby
        sample_std = np.std(sample, ddof=1)      # odchylenie standardowe (z korektą Bessela)

        # ✅ Przypadek 1: σ znane – używamy rozkładu normalnego
        z = norm.ppf(1 - alpha / 2)               # wartość z z rozkładu normalnego
        margin_known = z * sigma / np.sqrt(n)    # szerokość marginesu błędu
        ci_lower_known = sample_mean - margin_known
        ci_upper_known = sample_mean + margin_known

        # ✅ Sprawdzenie, czy prawdziwa wartość μ znajduje się w przedziale
        if ci_lower_known <= mu <= ci_upper_known:
            known_sigma_hits += 1

        # ✅ Przypadek 2: σ nieznane – używamy rozkładu t-Studenta
        t_critical = t.ppf(1 - alpha / 2, df=n - 1)        # wartość krytyczna t
        margin_unknown = t_critical * sample_std / np.sqrt(n)
        ci_lower_unknown = sample_mean - margin_unknown
        ci_upper_unknown = sample_mean + margin_unknown

        # ✅ Sprawdzenie, czy μ wpada do przedziału
        if ci_lower_unknown <= mu <= ci_upper_unknown:
            unknown_sigma_hits += 1

    # 📈 Obliczenie trafności (empirycznego poziomu ufności)
    coverage_known = known_sigma_hits / n_trials
    coverage_unknown = unknown_sigma_hits / n_trials

    # 📢 Wyświetlenie wyników
    print(f"\n📌 Rozmiar próby: n = {n}")
    print(f"→ σ znane:    Trafność = {coverage_known:.4f} (oczekiwane: 0.98)")
    print(f"→ σ nieznane: Trafność = {coverage_unknown:.4f} (oczekiwane: 0.98)")
