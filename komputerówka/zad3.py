# import numpy as np

# a_true = 0.5
# b = 1
# M = 100
# n_values = [10, 20, 1000]

# def generate_samples(N, a):
#     U = np.random.uniform(0, 1, N)
#     return U**(1/a)

# errors = []
# for N in n_values:
#     estimates = []
#     for _ in range(M):
#         X = generate_samples(N, a_true)
#         a_hat = -N / np.sum(np.log(X))
#         estimates.append(a_hat)

#     error = np.mean(np.abs(np.array(estimates) - a_true))
#     errors.append((N, error))

# for N, err in errors:
#     print(f"N = {N}: Średni błąd bezwzględny = {err:.5f}")

# Importujemy bibliotekę numpy – potrzebną do generowania próbek i obliczeń
import numpy as np

# Wartość prawdziwa parametru a – używana do generowania danych i porównywania z estymacją
a_true = 0.5

# Parametr b z treści zadania – zawsze równy 1
b = 1

# Liczba powtórzeń (symulacji) estymacji dla każdego rozmiaru próby (M z treści zadania)
M = 100

# Lista długości prób, dla których chcemy zbadać jakość estymatora
n_values = [10, 20, 1000]  # Z treści: N = 10, 20, ..., 1000 (tu tylko przykłady)

# Funkcja do generowania próby losowej X1,...,XN z rozkładu o dystrybuancie F(x) = x^a (dla b = 1)
# Odwracamy dystrybuantę: X = U^(1/a), gdzie U ∼ U(0,1)
def generate_samples(N, a):
    U = np.random.uniform(0, 1, N)   # Losujemy N liczb z rozkładu jednostajnego U(0,1)
    return U**(1/a)                  # Stosujemy transformację inwersyjną do otrzymania próby X

# Lista do przechowania błędów dla każdego N
errors = []

# Pętla po różnych długościach próby (N)
for N in n_values:
    estimates = []  # Lista do przechowania estymat dla danego N
    
    # Wykonujemy M niezależnych estymacji
    for _ in range(M):
        X = generate_samples(N, a_true)             # Generujemy próbkę z rozkładu F(x)
        a_hat = -N / np.sum(np.log(X))              # Obliczamy estymator parametru a ze wzoru w zadaniu
        estimates.append(a_hat)                     # Zapisujemy wynik estymacji

    # Obliczamy średni błąd bezwzględny estymatora względem a_true
    error = np.mean(np.abs(np.array(estimates) - a_true))
    
    # Zapisujemy wynik dla danego N
    errors.append((N, error))

# Wyświetlenie błędów dla każdej długości próby
for N, err in errors:
    print(f"N = {N}: Średni błąd bezwzględny = {err:.5f}")



