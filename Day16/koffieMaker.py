class KoffieMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "melk": 200,
            "koffie": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Melk: {self.resources['melk']}ml")
        print(f"Koffie: {self.resources['koffie']}g")

    def genoeg_recources(self, drank):
        genoeg = True
        for element in drank.ingredienten:
            if drank.ingredienten[element] > self.resources[element]:
                print(f"Niet genoeg  {element}")
                genoeg = False
        return genoeg

    def maak_koffie(self,order):
        for element in order.ingredienten:
            self.resources[element] -= order.ingredienten[element]
        print(f"Hier is jou {order.naam} !!!")
