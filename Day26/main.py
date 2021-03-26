# List compr

numbers = [1, 2, 3]
new_numbers = []
new_numbers = [n + 1 for n in numbers]

# String as list

name = "Milo"
letters_list = [letter for letter in name]

# Range list
range_list = [num * 2 for num in range(1, 5)]

# Conditional List
names = ["Lex", "Io", "Beth", "Caroline", "Eleanor", "Batista"]
short_names = [element for element in names if len(element) < 5]
capped_names = [element.upper() for element in names if len(element) > 5]
