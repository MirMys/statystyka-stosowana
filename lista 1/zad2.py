import numpy as np
import matplotlib.pyplot as plt
# A) Wykorzystując metodę odwrotnej dystrybuanty, wysymuluj prostą próbę losową o długości 1000
# z tego rozkładu dla wybranego zestawu parametrów (α i λ wybierz tak, aby wariancja była skończona).

# Parametry rozkładu Pareto (alpha > 2 aby wariancja była skończona)
alpha = 3
lmbda = 2
n = 1000  # liczba obserwacji

# Symulacja zmiennej losowej z rozkładu Pareto
U = np.random.uniform(0, 1, n)  # próbka z jednostajnego
X_pareto = lmbda * ((1 - U) ** (-1 / alpha) - 1)

# B) Wyznacz dystrybuantę empiryczną na podstawie wysymulowanej próby i porównaj ją z dystrybuantą teoretyczną.

# Posortowana próbka do rysowania dystrybuanty empirycznej
x_vals = np.sort(X_pareto)

# Liczba obserwacji mniejszych lub równych x (czyli ECDF)
empirical_cdf = np.arange(1, n + 1) / n  # [1/n, 2/n, ..., 1]

# Teoretyczna dystrybuanta
def pareto_cdf(x, alpha, lmbda):
    return 1 - (lmbda / (lmbda + x))**alpha

# Wartości teoretycznej dystrybuanty dla tych samych x
theoretical_cdf = pareto_cdf(x_vals, alpha, lmbda)

# Rysowanie obu dystrybuant
plt.figure(figsize=(8, 5))
plt.step(x_vals, empirical_cdf, where='post', label='Empiryczna dystrybuanta', color='blue')
plt.plot(x_vals, theoretical_cdf, label='Teoretyczna dystrybuanta', color='red')
plt.title('Porównanie dystrybuant: empiryczna vs teoretyczna')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.show()

# C) Przedstaw postać gęstości dla rozważanego rozkładu, a następnie porównaj ją z gęstością empiryczną.

# Funkcja gęstości rozkładu Pareto
def pareto_pdf(x, alpha, lmbda):
    return (alpha * lmbda**alpha) / (lmbda + x)**(alpha + 1)

# Zakres x do rysowania gęstości
x_range = np.linspace(min(X_pareto), max(X_pareto), 500)
theoretical_pdf = pareto_pdf(x_range, alpha, lmbda)

# Wykres: histogram empiryczny + gęstość teoretyczna
plt.figure(figsize=(8, 5))
plt.hist(X_pareto, bins=30, density=True, color='lightgray', edgecolor='black', label='Empiryczna gęstość (histogram)')
plt.plot(x_range, theoretical_pdf, color='red', label='Teoretyczna gęstość Pareto')
plt.title('Porównanie gęstości: empiryczna vs teoretyczna')
plt.xlabel('x')
plt.ylabel('gęstość')
plt.legend()
plt.grid(True)
plt.show()
