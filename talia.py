import random

class Talia:
    talia: list

    def __init__(self):
        znaki = ['♣', '♥', '♠', '♦']
        kart = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        tal = []
        for x in kart:
            tal.append(x + znaki[0])
            tal.append(x + znaki[1])
            tal.append(x + znaki[2])
            tal.append(x + znaki[3])
        self.talia = tal

    def pop(self, x):
        temp = self.talia[x]
        self.talia.remove(temp)
        return temp

    def __len__(self):
        return len(self.talia)

    def tasowanie(self):
        w = []
        polowa = int(len(self.talia) / 2)
        for i in range(polowa):
            w.append(self.talia[i])
            w.append(self.talia[polowa + i])
        self.talia = w

    def shuffle(self):
        cards = len(self.talia)
        for i in range(cards):
            j = random.randrange(i, cards)
            self.talia[i] = self.talia[j]

    def rozdanie(self):
        return self.talia.pop()

    def losowanie(self, ilosc = 2):
        lista = []
        tempL = self.talia.copy()
        if len(self.talia) == 52//ilosc:
            # for x in random.sample(range(1, 26), ):
            #     wyc = tempL[x]
            #     lista.append(wyc)
            return self.talia
            # for x in lista:
            #     self.talia.remove(x)
        for x in random.sample(range(1, 52), 52//ilosc):
            wyc = tempL[x]
            lista.append(wyc)
        for x in lista:
            self.talia.remove(x)
        return lista

    def losy(self, *gracze):
        ile = len(gracze)
        # while self.talia is None:
        #     self.




# talia = Talia()
# print(talia.talia)
# talia.tasowanie()
# print(talia.talia)
# talia = Talia()
# print(talia.talia)
#
# print(len(talia))
#
# # print(talia.losowanie())
# gracz1 = talia.losowanie()
# gracz2 = talia.losowanie()
# print(gracz1)
# # print("tali")
# print(gracz2)
# print(talia.talia)
# print(len(gracz1))