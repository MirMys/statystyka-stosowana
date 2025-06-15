# 3. Niech Z będzie zmienną losową z rozkładu Pareto z parametrami α > 0 oraz λ > 0. Zmienna losowa
# z rozkładu Burra z parametrami α > 0, λ > 0, τ > 0 jest zdefiniowana jako W = Z
# 1/τ

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import burr

# a) Wyznacz gęstość oraz dystrybuantę zmiennej losowej W.
# Parametry rozkładu Burra przez transformację Pareto
alpha = 3
lmbda = 2
tau = 2

# Dystrybuanta zmiennej W = Z^(1/tau)
def burr_cdf(w, alpha, lmbda, tau):
    return 1 - (lmbda / (lmbda + w**tau))**alpha

# Gęstość zmiennej W
def burr_pdf(w, alpha, lmbda, tau):
    return (alpha * tau * lmbda**alpha * w**(tau - 1)) / (lmbda + w**tau)**(alpha + 1)

# Zakres do rysowania
w_vals = np.linspace(0.01, 10, 500)

# Obliczenie wartości funkcji
cdf_vals = burr_cdf(w_vals, alpha, lmbda, tau)
pdf_vals = burr_pdf(w_vals, alpha, lmbda, tau)

# Wykres
plt.figure(figsize=(12, 5))

# Dystrybuanta
plt.subplot(1, 2, 1)
plt.plot(w_vals, cdf_vals, label='Dystrybuanta F_W(w)', color='blue')
plt.title('Dystrybuanta zmiennej W')
plt.xlabel('w')
plt.ylabel('F_W(w)')
plt.grid(True)
plt.legend()

# Gęstość
plt.subplot(1, 2, 2)
plt.plot(w_vals, pdf_vals, label='Gęstość f_W(w)', color='red')
plt.title('Gęstość zmiennej W')
plt.xlabel('w')
plt.ylabel('f_W(w)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# b) Wysymuluj 1000 niezależnych obserwacji odpowiadających zmiennej losowej W.
import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu
alpha = 3     # kształt
lmbda = 2     # skala
tau = 2       # parametr Burra

# Liczba próbek
n = 1000

# Generowanie próby Z ~ Pareto(α, λ)
# numpy.random.pareto(alpha) generuje próbki X z rozkładu Pareto(α) z minimalną wartością 1
X = np.random.pareto(alpha, n)  
Z = lmbda * (1 + X)  # skalujemy i przesuwamy próbkę, aby była z rozkładu Pareto(α, λ)

# Obliczenie próby W = Z^(1/tau)
W = Z ** (1 / tau)

# Wyświetlamy kilka wartości próby W
print(W[:10])


# c) Gęstość empiryczną wyznaczoną na podstawie wysymulowanej próby porównaj z gęstością teoretyczną zmiennej losowej W.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Parametry rozkładu (z poprzedniego podpunktu)
alpha = 3
lmbda = 2
tau = 2
n = 1000

# Generowanie próby Z ~ Pareto(α, λ)
X = np.random.pareto(alpha, n)
Z = lmbda * (1 + X)

# Obliczenie próby W = Z^(1/tau)
W = Z ** (1 / tau)

# Funkcja gęstości teoretycznej W
def burr_pdf(w, alpha, lmbda, tau):
    return (alpha * tau * lmbda**alpha * w**(tau - 1)) / (lmbda + w**tau)**(alpha + 1)

# Wyznaczanie gęstości empirycznej za pomocą KDE
kde = gaussian_kde(W)  # tworzymy estymator KDE na podstawie próby W

# Zakres wartości do wykresu
w_vals = np.linspace(min(W), max(W), 500)

# Obliczenie gęstości empirycznej i teoretycznej na tym samym zakresie
pdf_empirical = kde(w_vals)
pdf_theoretical = burr_pdf(w_vals, alpha, lmbda, tau)

# Wykres porównawczy
plt.figure(figsize=(8, 5))
plt.plot(w_vals, pdf_theoretical, label='Gęstość teoretyczna', color='red')
plt.plot(w_vals, pdf_empirical, label='Gęstość empiryczna (KDE)', color='blue', linestyle='--')
plt.title('Porównanie gęstości empirycznej i teoretycznej zmiennej W')
plt.xlabel('w')
plt.ylabel('gęstość f_W(w)')
plt.legend()
plt.grid(True)
plt.show()


# d) Dystrybuantę empiryczną wyznaczoną na podstawie wysymulowanej próby porównaj z dystrybuantą teoretyczną zmiennej losowej W.
import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu i próba z poprzednich podpunktów
alpha = 3
lmbda = 2
tau = 2
n = 1000

# Generowanie próby W
X = np.random.pareto(alpha, n)
Z = lmbda * (1 + X)
W = Z ** (1 / tau)

# Definicja dystrybuanty teoretycznej
def burr_cdf(w, alpha, lmbda, tau):
    return 1 - (lmbda / (lmbda + w**tau))**alpha

# Wyznaczenie dystrybuanty empirycznej (ECDF)
W_sorted = np.sort(W)                         # sortujemy próbę W rosnąco
ecdf = np.arange(1, n+1) / n                   # wartości ECDF od 1/n do 1

# Zakres do wykresu - wartości unormowane do próby
w_vals = np.linspace(min(W), max(W), 500)

# Dystrybuanta teoretyczna na siatce
cdf_theoretical = burr_cdf(w_vals, alpha, lmbda, tau)

# Wykres porównawczy
plt.figure(figsize=(8,5))
plt.step(W_sorted, ecdf, where='post', label='Dystrybuanta empiryczna (ECDF)', color='blue')
plt.plot(w_vals, cdf_theoretical, label='Dystrybuanta teoretyczna', color='red')
plt.title('Porównanie dystrybuanty empirycznej i teoretycznej zmiennej W')
plt.xlabel('w')
plt.ylabel('F_W(w)')
plt.legend()
plt.grid(True)
plt.show()

