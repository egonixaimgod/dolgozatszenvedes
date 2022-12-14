#Készítette: Bodnár Bence, 2022.12.14.
import math
class HengerTerfogat:
    def __init__ (self, sugar = 4, magassag = 3):
        self.sugar = sugar
        self.magassag = magassag

    def hTerfogat (self):
        terfogatkiszamolas = print(math.pow(self.sugar, 2) * math.pi * self.magassag)
        return terfogatkiszamolas