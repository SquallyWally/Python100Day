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

    optie = input("What would you like? ( espresso/latte/cappuccino): ")

    # Print Report
    if optie == "r":
        koffieMaker.report()
    elif optie == "off":
        break
    else:
        # Check Resources
        drank = menu.find_drank(optie)
        if koffieMaker.genoeg_recources(drank):

            # Process Coins
            prijs = menu.find_price(optie)
            # check Transaction if succesfull
            print("kek")
            if geldMachine.betaling(prijs):
                # Make Cafe
                koffieMaker.maak_koffie(drank)
