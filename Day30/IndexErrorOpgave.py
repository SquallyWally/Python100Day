fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(0)
make_pie(1)
make_pie(2)
make_pie(3)
make_pie(4)
