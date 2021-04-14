import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_new_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


# print(nato_new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_stuff():
    word = input("Enter a word: ").upper()

    try:
        output = [nato_new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_stuff()
    else:
        print(output)


generate_stuff()
