class GeldMachine:
    VALUTA = "$"

    MUNT_WAADES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.winst = 0
        self.geld_ontvangen = 0

    def report(self):
        print(f"Geld: {self.VALUTA} {self.winst}")

    def munten_verwerken(self):
        print("Voeg munten toe: ")
        for munt in self.MUNT_WAADES:
            self.geld_ontvangen += int(input(f"Hoeveel {munt}?: ")) * self.MUNT_WAADES[munt]
        return self.geld_ontvangen

    def betaling(self, betaling):

        self.munten_verwerken()
        if self.geld_ontvangen >= betaling:
            restant = round(self.geld_ontvangen - betaling, 2)
            print(f"hier is jou wisselgeld {self.VALUTA} {restant}")

            self.winst += betaling
            self.geld_ontvangen = 0
            return True
        else:
            verschil = betaling - self.geld_ontvangen
            print(f"Je heb niet genoeg geld, je bent nog {self.VALUTA}{verschil} tekort")

            self.geld_ontvangen = 0
            return False
