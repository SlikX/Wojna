from talia import Talia
from gracz import Gracz
from karta import Karta
import random

def main():
    # print("Hell")
    # for x in random.sample(range(1,14), 9):
    #     print(x)

    # talia = Talia()
    ilosc_graczy = 2
    # gracz1 = Gracz("gracz1", talia.losowanie(), len(talia))
    # print(gracz1.imie)
    # print(gracz1.karty)
    # print(gracz1.ile_kart)
    # gracz2 = Gracz("gracz2", talia.losowanie(), len(talia))
    # print(gracz2.imie)
    # print(gracz2.karty)
    # print(gracz2.ile_kart)

    # talia = Talia()
    # print(talia.talia)
    # Tasowanie
    # Trzeba zmienic metode tasowania bo nie działa jak powinna
    # talia.tasowanie()
    # talia.tasowanie()
    # talia.tasowanie()
    # talia.tasowanie()
    # talia.tasowanie()
    # talia.shuffle()
    #
    #
    # print(talia.talia)
    # # Dodanie graczy
    # gracz1 = Gracz('Gracz1', [])
    # gracz2 = Gracz('Gracz2', [])
    # for x in range(52):
    #     if x % 2 == 0:
    #         gracz1.karty.append(talia.rozdanie())
    #     else:
    #         gracz2.karty.append(talia.rozdanie())
    # print(gracz1.karty)
    # print(gracz2.karty)
    # Rozdawanie kart

    nowa_talia = Talia()
    print(nowa_talia)


if __name__ == '__main__':
    main()