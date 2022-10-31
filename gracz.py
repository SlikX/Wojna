from talia import Talia
# Gracz
class Gracz:
    imie: str
    karty: list
    # ile_kart: int

    def __init__(self, imie, karty):
        self.imie = imie
        self.karty = karty
        # self.ile_kart = ile_kart
        # self.akt_karta = akt_karta

