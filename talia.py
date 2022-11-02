import karta
import random
from karta import Karta

class Talia:
    nowa_Talia = []

    def __init__(self):
        for x in range(13):
            self.nowa_Talia.append(Karta(znak=0, karta=x))
            self.nowa_Talia.append(Karta(znak=1, karta=x))
            self.nowa_Talia.append(Karta(znak=2, karta=x))
            self.nowa_Talia.append(Karta(znak=3, karta=x))

    def rozdanie(self):
        return self.nowa_Talia.pop()

    def tasowanie(self):
        for x in range(len(self.nowa_Talia)):
            tem = random.randrange(x ,len(self.nowa_Talia))
            pom = self.nowa_Talia[x]
            self.nowa_Talia[x] = self.nowa_Talia[tem]
            self.nowa_Talia[tem] = pom


def drukuj(nowa):
    s = ""
    for x in range(len(nowa.nowa_Talia)):
        s = ""
        x = nowa.nowa_Talia[x].__str__()
        s = s + str(x) + " "
    print("\n")
# nowa = Talia()
# drukuj()

