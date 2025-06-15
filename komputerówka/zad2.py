# import numpy as np
# import matplotlib.pyplot as plt

# a = 0.5
# b = 2
# N = 1000
# M = 10000

# U_values = []
# for i in range(M):
#     U = np.random.uniform(0, 1, N)
#     X = (1 - (1 - U)**(1/b))**(1/a)
#     U_values.append(np.max(X))

# U_values = np.array(U_values)

# plt.figure(figsize=(10, 6))
# plt.hist(U_values, bins=25, alpha=0.7, edgecolor='black', label='Histogram U')
# plt.title('Histogram Maksymalnych Wartości U')
# plt.xlabel('u')
# plt.ylabel('Częstość')
# plt.grid(True)
# plt.show()

# u_sorted = np.sort(U_values)
# ecdf_y = np.arange(1, M + 1) / M
# ecdf_x = u_sorted

# x_values = np.linspace(0, 1, 1000)
# F_x = 1 - (1 - x_values**a)**b
# G_x = F_x**N

# plt.figure(figsize=(10, 6))
# plt.plot(ecdf_x, ecdf_y, label='Empiryczna Dystrybuanta U')
# plt.step(x_values, G_x, 'r--', label='Teoretyczna Dystrybuanta U')
# plt.xlabel('x')
# plt.ylabel('F(x)')
# plt.title('Porównanie Dystrybuanty Empirycznej i Teoretycznej U')
# plt.legend()
# plt.grid(True)
# plt.show()

# print("Obie dystrybuanty pokrywają się co oznacza że rozkład maksimum próby rzeczywiście odpowiada przewidywaniom teoretycznym i potwierdza poprawnosc zastosowanej metody")

# Importujemy potrzebne biblioteki:
# numpy – do operacji numerycznych i losowania danych
# matplotlib.pyplot – do tworzenia wykresów
import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu (z treści zadania)
a = 0.5  # parametr a rozkładu
b = 2    # parametr b rozkładu
N = 1000 # liczność pojedynczej próby
M = 10000 # liczba powtórzeń (symulacji) – czyli liczba prób losowych

# Lista do przechowywania wartości maksymalnych z każdej z M prób
U_values = []

# Pętla powtarzająca eksperyment M razy
for i in range(M):
    # Losowanie N liczb z rozkładu jednostajnego U(0,1)
    U = np.random.uniform(0, 1, N)
    
    # Transformacja z rozkładu jednostajnego na dany rozkład X,
    # korzystając ze wzoru odwrotnej dystrybuanty (metoda inwersji)
    X = (1 - (1 - U)**(1/b))**(1/a)
    
    # Zapisz maksymalną wartość z wygenerowanej próby X
    U_values.append(np.max(X))

# Konwersja listy na tablicę numpy do dalszej analizy
U_values = np.array(U_values)

# Rysowanie histogramu maksymalnych wartości z prób
plt.figure(figsize=(10, 6))
plt.hist(U_values, bins=25, alpha=0.7, edgecolor='black', label='Histogram U')
# bins=25 oznacza, że dzielimy oś X na 25 przedziałów klasowych, zgodnie z treścią zadania 2

plt.title('Histogram Maksymalnych Wartości U')
plt.xlabel('u')            # Oś X opisuje wartości maksymalne z prób
plt.ylabel('Częstość')     # Oś Y – liczba wystąpień wartości w danym przedziale
plt.grid(True)             # Włączenie siatki na wykresie
plt.show()                 # Wyświetlenie histogramu

# Budowa dystrybuanty empirycznej (ECDF) z danych U_values
u_sorted = np.sort(U_values)                 # Sortujemy dane rosnąco
ecdf_y = np.arange(1, M + 1) / M             # Dla każdej wartości przypisujemy i/M
ecdf_x = u_sorted                            # Osie X i Y dystrybuanty empirycznej

# Przygotowanie teoretycznej dystrybuanty rozkładu maksimum
x_values = np.linspace(0, 1, 1000)           # Siatka punktów do wykresu G(x)

# Obliczenie F(x): teoretyczna dystrybuanta pojedynczej zmiennej losowej X
F_x = 1 - (1 - x_values**a)**b

# Obliczenie G(x): teoretyczna dystrybuanta maksimum z próby – G(x) = [F(x)]^N
G_x = F_x**N

# Porównanie dystrybuant: empirycznej (ECDF) i teoretycznej (G)
plt.figure(figsize=(10, 6))
plt.plot(ecdf_x, ecdf_y, label='Empiryczna Dystrybuanta U')  # ECDF jako linia ciągła
plt.step(x_values, G_x, 'r--', label='Teoretyczna Dystrybuanta U')  # Teoretyczna jako linia przerywana
plt.xlabel('x')                    # Oś X – wartości zmiennej losowej
plt.ylabel('F(x)')                 # Oś Y – wartości dystrybuanty
plt.title('Porównanie Dystrybuanty Empirycznej i Teoretycznej U')
plt.legend()
plt.grid(True)
plt.show()

# Wydrukowanie podsumowania wniosku
print("Obie dystrybuanty pokrywają się co oznacza że rozkład maksimum próby rzeczywiście odpowiada przewidywaniom teoretycznym i potwierdza poprawnosc zastosowanej metody")
