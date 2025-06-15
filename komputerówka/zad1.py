# import numpy as np
# import matplotlib.pyplot as plt

# a = 0.5
# b = 2 
# N = 1000

# U = np.random.uniform(0, 1, N)
# X = (1-(1-U)**(1/b))**(1/a)

# X_sorted = np.sort(X)

# empiryczna = np.arange(1, N + 1) / N 

# x_values = np.linspace(0, 1, 1000)
# F_x = 1 - (1 - x_values**a)**b


# średnia = np.mean(X)
# mediana = np.median(X)
# odchylenie_standardowe = np.std(X)
# print(f"Średnia: {średnia}")
# print(f"Mediana: {mediana}")    
# print(f"Odchylenie standardowe: {odchylenie_standardowe}")

# plt.figure(figsize=(10, 6))
# plt.step(X_sorted, empiryczna, label='Dystrybuanta Empiryczna', where='post')
# plt.plot(x_values, F_x, 'r--', label='Dystrybuanta Teoretyczna')
# plt.xlabel('x')
# plt.ylabel('F(x)')
# plt.title('Porównanie Dystrybuanty Empirycznej i Teoretycznej')
# plt.legend()
# plt.grid(True)
# plt.show()

# Importujemy potrzebne biblioteki:
# numpy – do obliczeń matematycznych i generowania losowych danych
# matplotlib.pyplot – do tworzenia wykresów
import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładu
a = 0.5  # parametr a z definicji rozkładu
b = 2    # parametr b z definicji rozkładu
N = 1000 # liczność próby (czyli ile losowych wartości generujemy)

# Krok 1: Generowanie próby losowej z rozkładu jednostajnego na przedziale (0,1)
# Używamy rozkładu jednostajnego, bo chcemy zastosować metodę odwrotnej dystrybuanty
U = np.random.uniform(0, 1, N)

# Krok 2: Transformacja próby U na zmienną losową X o zadanym rozkładzie
# Zastosowano wzór na odwrotność dystrybuanty:
# X = (1 - (1 - U)^(1/b))^(1/a)
# Ten wzór wynika z przekształcenia F(x) = 1 - (1 - x^a)^b
X = (1 - (1 - U)**(1/b))**(1/a)

# Krok 3: Posortuj dane, żeby przygotować dane do rysowania dystrybuanty empirycznej
X_sorted = np.sort(X)

# Krok 4: Zbuduj dystrybuantę empiryczną – jej wartości to i/N
# Czyli dla każdej wartości w posortowanej próbie przypisujemy i/N, gdzie i to numer wartości
empiryczna = np.arange(1, N + 1) / N

# Krok 5: Zbuduj siatkę punktów x do narysowania teoretycznej dystrybuanty
x_values = np.linspace(0, 1, 1000)  # 1000 równomiernie rozłożonych punktów od 0 do 1

# Krok 6: Oblicz wartości teoretycznej dystrybuanty F(x) dla punktów x_values
# F(x) = 1 - (1 - x^a)^b – to teoretyczna dystrybuanta z treści zadania
F_x = 1 - (1 - x_values**a)**b

# Krok 7: Oblicz podstawowe statystyki z próby X
średnia = np.mean(X)               # Średnia arytmetyczna próby
mediana = np.median(X)             # Mediana (wartość środkowa)
odchylenie_standardowe = np.std(X) # Odchylenie standardowe (rozproszenie danych)

# Wypisz statystyki do konsoli
print(f"Średnia: {średnia}")
print(f"Mediana: {mediana}")    
print(f"Odchylenie standardowe: {odchylenie_standardowe}")

# Krok 8: Narysuj wykres porównujący dystrybuantę empiryczną i teoretyczną

plt.figure(figsize=(10, 6))  # Rozmiar wykresu

# Wykres dystrybuanty empirycznej – wykres schodkowy
plt.step(X_sorted, empiryczna, label='Dystrybuanta Empiryczna', where='post')

# Wykres dystrybuanty teoretycznej – wykres liniowy przerywany (czerwony)
plt.plot(x_values, F_x, 'r--', label='Dystrybuanta Teoretyczna')

# Etykiety osi
plt.xlabel('x')
plt.ylabel('F(x)')

# Tytuł wykresu
plt.title('Porównanie Dystrybuanty Empirycznej i Teoretycznej')

# Legenda i siatka
plt.legend()
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
