
class Karta:
    znaki = ['♣', '♥', '♠', '♦']
    karty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, znak: int, karta: int):
        self.znaki = znak
        self.karty = karta

    def __str__(self):
        print(str(Karta.znaki[self.znaki]) + str(Karta.karty[self.karty]), end=" ")

    # def porownaj(self, gracz2):
    #     if self.karty < gracz2.karty:
    #
