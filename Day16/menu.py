class MenuItem:
    def __init__(self, naam, water, melk, koffie, cost):
        self.naam = naam
        self.cost = cost
        self.ingredienten = {
            "water": water,
            "melk": melk,
            "koffie": koffie
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(naam="latte", water=200, melk=150, koffie=24, cost=2.5),
            MenuItem(naam="cappuccino", water=250, melk=50, koffie=24, cost=3),
            MenuItem(naam="espresso", water=50, melk=0, koffie=18, cost=1.5),

        ]

    def get_elements(self):
        opties = ""
        for element in self.menu:
            opties += f"{element.naam}/"
        return opties

    def find_drank(self,order_name):
        for element in self.menu:
            if element.naam == order_name:
                return element
        print("Sorry maar deze drank is niet meer beschikbaar")

    def find_price(self,order_name):
        for element in self.menu:
            if element.naam == order_name:
                return element.cost
