from koffieMaker import KoffieMaker
from menu import Menu,MenuItem

from geldMachine import GeldMachine

# Print Report
# Check Resources
# Process Coins
# check Transaction if succesfull
# Make Cafe

koffieMaker = KoffieMaker()
menu = Menu()
geldMachine = GeldMachine()

while True:
    optie = menu.get_elements()
    keuze = input(f"What would you like? ( {optie}): ")

    # Print Report
    if keuze == "r":
        koffieMaker.report()
        geldMachine.report()
    elif keuze == "off":
        break
    else:
        # Check Resources
        drank = menu.find_drank(keuze)
        if koffieMaker.genoeg_recources(drank):

            # Process Coins
            prijs = menu.find_price(keuze)
            # check Transaction if succesfull
            print("kek")
            if geldMachine.betaling(prijs):
                # Make Cafe
                koffieMaker.maak_koffie(drank)
