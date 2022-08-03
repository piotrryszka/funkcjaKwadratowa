from kwadratowa import FunkcjaKwadratowa
def main():
    f1 = FunkcjaKwadratowa(3, 4, -7)
    f1.wypisz()
    print('y=', f1.oblicz_wartosc(2))
    print('y=', f1.oblicz_wartosc(-2))

    print(FunkcjaKwadratowa(0, 0, 0).rozwiaz())
    print(FunkcjaKwadratowa(0, 0, 18).rozwiaz())
    print(FunkcjaKwadratowa(0, 5, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, -5, 6).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())

if __name__ == "__main__":
    main()