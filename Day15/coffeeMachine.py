MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
aan = True
geld = 0.0


def berekenMunten():
    """"Returns total calculated coins"""
    print("Voeg munten toe: ")
    totaal = int(input("Hoeveel quarters?: ")) * 0.25
    totaal += int(input("Hoeveel dimes?: ")) * 0.10
    totaal += int(input("Hoeveel nickles?: ")) * 0.05
    totaal += int(input("Hoeveel pennies?: ")) * 0.01
    print(totaal)
    return totaal


def heeftGenoegIngredienten(ingredient):
    for element in ingredient:
        if ingredient[element] >= resources[element]:  # dus als er meer ingredientne zijn dan resources
            print(f"Niet genoeg  {element}")
            return False
    return True


def maakKoffie(drank_naam, ingredienten):
    """Deduct the req ingredients from the resources"""
    for element in ingredienten:
        resources[element] -= ingredienten[element]
    print(f"Hier is jou {drank_naam} !!!")


def genoegGeld(betaling, drank_prijs):
    if drank_prijs > betaling:

        restant = round(drank_prijs - betaling, 2)
        print(f"Je heb niet genoeg geld, je bent nog {restant} tekort")
        return False
    else:
        print("Success")
        global geld

        wisselgeld = round(betaling - drank_prijs, 2)
        geld += drank_prijs
        print(f"hier is jou wisselgeld {wisselgeld}")
        return True


while aan:

    optie = input("What would you like? ( espresso/latte/cappuccino): ")

    if optie == "r":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print("Geld:", "$%s" % geld)
    elif optie == "off":
        break
    else:
        drank = MENU[optie]
        if heeftGenoegIngredienten(drank['ingredients']):
            betaling = berekenMunten()
            if genoegGeld(betaling, drank['cost']):
                maakKoffie(optie, drank['ingredients'])
