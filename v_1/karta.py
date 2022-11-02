import random

class Karta:
    znak = ['♣', '♥', '♠', '♦']
    karta = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, znak, karta):
        self.znak = znak
        self.karta = karta

    def __str__(self):
        return str(Karta.karta[self.karta]) + str(Karta.znak[self.znak])

# karta = Karta(0,0)
# print(karta.__str__())