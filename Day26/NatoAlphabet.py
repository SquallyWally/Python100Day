import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_new_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(nato_new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [nato_new_dict[letter] for letter in word]
print(output)
