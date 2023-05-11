# Dzień 76 Docstings - Komentarze

# To jest komentarz jednolinijkowy
x = 5 # Przypisujemy wartość 5 do zmiennej x

"""
To jest komentarz
wielolinijkowy. Możemy tu
pisać dowolnie wiele linii.
"""

'''
To jest kolejny sposób na
zapisanie komentarza
wielolinijkowego.
'''
# Docstrings
def add(a, b):
    """
    Dodaje dwie liczby i zwraca wynik.

    Argumenty:
    a -- pierwsza liczba
    b -- druga liczba

    Zwraca:
    Suma liczb a i b.
    """
    return a + b

# Wyświetlenie dokumentacji dla wbudowanej funkcji print
help(print)

# Wyświetlenie dokumentacji dla funkcji add
help(add)

# Wyświetlenie dokumentacji dla klasy list
help(list)

# Zadanie: Dodaj docstringową dokumentację do kalkulatora

import os

def perform_calculation(num1, num2, operator):
    """"""
    Dodaje dwie liczby i zwraca wynik.
    if operator == "+":
        return num1 + num2
    """"""
    """"""
    Odejmuje dwie liczby i zwraca wynik.
    elif operator == "-":
        return num1 - num2
    """"""
    """"""
    Mnoży dwie liczby i zwraca wynik.
    elif operator == "*":
        return num1 * num2
    """"""
    """"""
    Dzieli dwie liczby i zwraca
    elif operator == "/":
        return num1 / num2
    """"""
    else:
        return "invalid operator"