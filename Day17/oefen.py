class Gebruiker:
    def __init__(self, gebruiker_id, naam):
        self.id = gebruiker_id
        self.naam = naam
        self.volgers = 0
        self.followers = 0

    def follow(self,gebruiker):
        gebruiker.volgers += 1
        self.followers += 1


gebruiker_1 = Gebruiker("01", "Milo")
gebruiker_2 = Gebruiker("02", "Isa")

print(gebruiker_1.naam)
print(gebruiker_1.id)
print(gebruiker_1.volgers)


gebruiker_2.follow(gebruiker_1)
print(gebruiker_1.volgers)