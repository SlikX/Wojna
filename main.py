import talia
from karta import Karta
from talia import Talia
from gracz import Gracz

def main():
    print("Gra w WOJNE")
    # poj_karta = Karta(0,0)
    # poj_karta.__str__()

    new = Talia()
    talia.drukuj(new)
    new.tasowanie()
    talia.drukuj(new)
    new.rozdanie()
    # x.__str__()
    talia.drukuj(new)

    gracz1 = Gracz("gracz1")
    gracz2 = Gracz("Gracz2")
    # print(gracz1.ile_kart)



if __name__ == '__main__':
    main()