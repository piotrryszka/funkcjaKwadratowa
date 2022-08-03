import math


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"y={self.a}*x^2+{self.b}*x+{self.c}")

    def oblicz_wartosc(self, x):
        return self.a * x * x + self.b * x + self.c

    def rozwiaz(self):
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return 'Nieskończona liczba rozwiązań, wynikiem jest fukncja stała y=0'
            else:
                return 'Nie ma rozwiązań, stała y nie przecina się z osią x.'
        if self.a == 0:
            return 'współczynnik a równy 0 więc jest jedno roziązanie', -self.c / self.b
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta < 0:
            return 'Nie ma miejsc zerowych ponieważ delta mniejsza od 0.'
        elif delta == 0:
            return -self.b / (2 * self.a), "Delta równia 0 wiec jedno rozwiązanie"
        return (-self.b - math.sqrt(delta)) / (2 * self.a), (-self.b + math.sqrt(delta)) / (2 * self.a)
