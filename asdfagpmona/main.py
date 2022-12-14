#Készítette: Bodnár Bence, 2022.12.14.
from hengerFelszin import HengerFelszin
from hengerTerfogat import HengerTerfogat
class Main:
    def __init__(self, sugar = 0, magassag = 0):
        self.sugar = sugar
        self.magassag = magassag

    def informacio (self):
        print("Készítette: Bodnár Bence, 2022.12.14., a program egy adott henger felszínét és térfogatát számolja ki.")

    def beker (self):
        self.sugar = float(input("Kérem adja meg a henger sugarát: "))
        self.magassag = float(input("Kérem adja meg a henger magasságát: "))

    def chooser (self):
        valasztas = int(input("Melyiket szeretne számolni? Felszín [1] Térfogat [2]\n"))

        if valasztas == 1:
            felszin.hFelszin()
        
        elif valasztas == 2:
            terfogat.hTerfogat()
        
        else:
            print("A beírt szám hibás!")
            


felszin = HengerFelszin()
terfogat = HengerTerfogat()
main = Main()

main.beker()
main.informacio()
main.chooser()



