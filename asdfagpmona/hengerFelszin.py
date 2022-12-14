#Készítette: Bodnár Bence, 2022.12.14.
import math
class HengerFelszin:
    def __init__(self, sugar = 5, magassag = 3):
        self.sugar = sugar
        self.magassag = magassag

    def hFelszin (self):
        felszinkiszamolas = print(2 * self.sugar * math.pi + 2 * self.sugar * math.pi * self.magassag)
        return felszinkiszamolas
