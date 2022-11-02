
class Gracz:
    imie: str
    karty = []
    ile_kart = 0

    def __init__(self, imie, karty = []):
        self.imie = imie
        self.karty = karty
        self.ile_kart = len(karty)

