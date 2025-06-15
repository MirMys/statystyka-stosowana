# 2. Rozpatrzmy próbę prostą X1, ..., Xn oraz statystykę U = max{X1, ..., Xn}. Znajdź rozkład statystyki
# U dla próby z następujących rozkładów:
# (a) normalnego,
# (b) lognormalnego,
# (c) Pareto.
# Narysuj dystrybuanty empiryczne statystyki U dla rozpatrywanych rozkładów


# 📦 Import wymaganych bibliotek
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Ustawienia ogólne
n = 1000                     # liczność próby
np.random.seed(42)          # ustalenie ziarna losowości

# 📊 Generowanie prób z trzech rozkładów

# 1. Normalny: N(0,1)
sample_normal = np.random.normal(loc=0, scale=1, size=n)

# 2. Lognormalny: LogN(0,1)
sample_lognormal = np.random.lognormal(mean=0, sigma=1, size=n)

# 3. Pareto(α=3), przesunięty o 1 (bo domyślny początek to x=1)
alpha = 3
sample_pareto = (np.random.pareto(a=alpha, size=n) + 1)

# 📈 Statystyka: maksimum w próbie
U_normal = np.max(sample_normal)
U_lognormal = np.max(sample_lognormal)
U_pareto = np.max(sample_pareto)

# 🖨️ Wyświetlenie wartości maksymalnych (dla informacji)
print(f"Maksimum z próby (normalny): {U_normal:.4f}")
print(f"Maksimum z próby (lognormalny): {U_lognormal:.4f}")
print(f"Maksimum z próby (Pareto): {U_pareto:.4f}")

# 🔁 Powtórzenie eksperymentu wielokrotnie, aby uzyskać rozkład statystyki U
num_trials = 10000                     # liczba prób
max_normal = []
max_lognormal = []
max_pareto = []

for _ in range(num_trials):
    max_normal.append(np.max(np.random.normal(0, 1, n)))
    max_lognormal.append(np.max(np.random.lognormal(0, 1, n)))
    max_pareto.append(np.max(np.random.pareto(alpha, n) + 1))

# 📈 Tworzenie wykresów rozkładów statystyki U
plt.figure(figsize=(12, 6))
sns.kdeplot(max_normal, label='Normalny', color='blue', lw=2)
sns.kdeplot(max_lognormal, label='Lognormalny', color='green', lw=2)
sns.kdeplot(max_pareto, label='Pareto', color='red', lw=2)

# ✨ Opisy i legenda
plt.title('Empiryczne rozkłady statystyki U = max(X₁, ..., Xₙ)', fontsize=14)
plt.xlabel('Wartość statystyki U (maximum)', fontsize=12)
plt.ylabel('Gęstość empiryczna', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# 📊 Wyświetlenie wykresu
plt.show()
