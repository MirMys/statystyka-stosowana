import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Rozpatrzymy zmienną losową zdefiniowaną jako Y = exp(X), gdzie X ∼ N(µ, σ). Wówczas zmienna
# losowa Y ma rozkład log-normalny, tj. Y ∼ LN(µ, σ).
# A) Wyznacz dystrybuantę zmiennej losowej Y i wyraź ją w języku dystrybuanty standardowego rozkładu normalnego.

# Parametry rozkładu normalnego X ~ N(mu, sigma)
mu = 0
sigma = 1

# Przedział y dla którego obliczymy dystrybuantę
y_vals = np.linspace(0.01, 5, 500)  # Y > 0, nie może być 0

# Dystrybuanta zmiennej losowej Y = exp(X)
# F_Y(y) = P(Y <= y) = P(X <= log(y)) = Phi((log(y) - mu) / sigma)
F_Y_vals = norm.cdf((np.log(y_vals) - mu) / sigma)

# Rysujemy wykres dystrybuanty
plt.figure(figsize=(8, 5))
plt.plot(y_vals, F_Y_vals, label='Dystrybuanta F_Y(y)')
plt.xlabel('y')
plt.ylabel('F_Y(y)')
plt.title('Dystrybuanta zmiennej losowej Y ~ LN(μ, σ)')
plt.grid(True)
plt.legend()
plt.show()

# B) Wyznacz gęstość zmiennej losowej Y .

# Gęstość zmiennej losowej Y = e^X, czyli rozkład log-normalny
def lognormal_pdf(y, mu, sigma):
    # Zwraca wartość gęstości log-normalnej
    return (1 / (y * sigma * np.sqrt(2 * np.pi))) * np.exp(-((np.log(y) - mu) ** 2) / (2 * sigma ** 2))

# Obliczenie gęstości dla zadanych wartości y
pdf_vals = lognormal_pdf(y_vals, mu, sigma)

# Wykres gęstości
plt.figure(figsize=(8, 5))
plt.plot(y_vals, pdf_vals, label='Gęstość f_Y(y)', color='orange')
plt.xlabel('y')
plt.ylabel('f_Y(y)')
plt.title('Gęstość zmiennej losowej Y ~ LN(μ, σ)')
plt.grid(True)
plt.legend()
plt.show()

# C) Zaproponuj metodę symulacji zmiennej losowej Y
# Ustawiamy parametry
mu = 0
sigma = 1
n = 10000  # liczba próbek

# Symulujemy zmienną X z rozkładu normalnego
X_samples = np.random.normal(mu, sigma, n)

# Symulujemy zmienną Y = exp(X), czyli log-normalną
Y_samples = np.exp(X_samples)


# D) Dla danych odpowiadających zmiennym X oraz Y narysuj histogramy liczności oraz częstości.
# Histogram liczności dla X
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(X_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram liczności zmiennej X')
plt.xlabel('X')
plt.ylabel('Liczność')
plt.grid(True)

# Histogram liczności dla Y
plt.subplot(1, 2, 2)
plt.hist(Y_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram liczności zmiennej Y')
plt.xlabel('Y')
plt.ylabel('Liczność')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histogram częstości (density=False, ale dzielimy przez n)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
counts, bins, _ = plt.hist(X_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram częstości zmiennej X')
plt.xlabel('X')
plt.ylabel('Częstość')
plt.grid(True)
# Przeliczamy liczność na częstość
plt.clf()  # czyścimy subplot do poprawnego rysowania
plt.bar(bins[:-1], counts / n, width=np.diff(bins), align='edge', color='skyblue', edgecolor='black')

plt.subplot(1, 2, 2)
counts, bins, _ = plt.hist(Y_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram częstości zmiennej Y')
plt.xlabel('Y')
plt.ylabel('Częstość')
plt.grid(True)
plt.clf()
plt.bar(bins[:-1], counts / n, width=np.diff(bins), align='edge', color='lightgreen', edgecolor='black')

plt.tight_layout()
plt.show()

# E) Dla danych odpowiadających zmiennym X oraz Y narysuj unormowane histogramy w taki sposób,
# aby mogły być one porównane z gęstościami teoretycznymi odpowiednich zmiennych losowych.
# Na wykresach z unormowanymi histogramami narysuj również teoretyczne gęstości zmiennych
# losowych X oraz Y .

# Zakresy do rysowania gęstości
x_vals = np.linspace(min(X_samples), max(X_samples), 500)
y_vals_plot = np.linspace(min(Y_samples), max(Y_samples), 500)

# Gęstości teoretyczne
f_X = norm.pdf(x_vals, mu, sigma)
f_Y = lognormal_pdf(y_vals_plot, mu, sigma)

# Histogramy unormowane + teoretyczne gęstości
plt.figure(figsize=(12, 5))

# Dla zmiennej X
plt.subplot(1, 2, 1)
plt.hist(X_samples, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.6, label='Histogram X (normowany)')
plt.plot(x_vals, f_X, 'r', label='Teoretyczna gęstość X')
plt.title('Zmienna X ~ N(μ, σ)')
plt.xlabel('x')
plt.ylabel('gęstość')
plt.legend()
plt.grid(True)

# Dla zmiennej Y
plt.subplot(1, 2, 2)
plt.hist(Y_samples, bins=30, density=True, color='lightgreen', edgecolor='black', alpha=0.6, label='Histogram Y (normowany)')
plt.plot(y_vals_plot, f_Y, 'r', label='Teoretyczna gęstość Y')
plt.title('Zmienna Y ~ LN(μ, σ)')
plt.xlabel('y')
plt.ylabel('gęstość')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()



# F) Dla danych odpowiadających zmiennym X oraz Y wyznacz gęstości empiryczne przy pomocy
# estymatora jądrowego. Na wykresach z gęstościami empirycznymi narysuj również teoretyczne
# gęstości odpowiadające zmiennym losowym X oraz Y .

from scipy.stats import gaussian_kde

# Estymator jądrowy dla X i Y
kde_X = gaussian_kde(X_samples)
kde_Y = gaussian_kde(Y_samples)

# Wartości x i y do rysowania estymowanych gęstości
x_vals = np.linspace(min(X_samples), max(X_samples), 500)
y_vals_plot = np.linspace(min(Y_samples), max(Y_samples), 500)

# Obliczenie estymowanych gęstości
kde_X_vals = kde_X(x_vals)
kde_Y_vals = kde_Y(y_vals_plot)

# Teoretyczne gęstości
f_X = norm.pdf(x_vals, mu, sigma)
f_Y = lognormal_pdf(y_vals_plot, mu, sigma)

# Wykresy
plt.figure(figsize=(12, 5))

# Dla zmiennej X
plt.subplot(1, 2, 1)
plt.plot(x_vals, kde_X_vals, label='Empiryczna gęstość KDE X', color='blue')
plt.plot(x_vals, f_X, label='Teoretyczna gęstość X', color='red', linestyle='--')
plt.title('Gęstość X: empiryczna vs teoretyczna')
plt.xlabel('x')
plt.ylabel('gęstość')
plt.legend()
plt.grid(True)

# Dla zmiennej Y
plt.subplot(1, 2, 2)
plt.plot(y_vals_plot, kde_Y_vals, label='Empiryczna gęstość KDE Y', color='green')
plt.plot(y_vals_plot, f_Y, label='Teoretyczna gęstość Y', color='red', linestyle='--')
plt.title('Gęstość Y: empiryczna vs teoretyczna')
plt.xlabel('y')
plt.ylabel('gęstość')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
