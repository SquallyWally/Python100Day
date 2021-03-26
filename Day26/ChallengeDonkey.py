nummers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# list where each number is squared
# new_list = [new_item for item in list]
squared_numbers = [item * item for item in nummers]

print(squared_numbers)

#prints only evven numbers
even_numbers = [item for item in nummers if item % 2 == 0]

print(even_numbers)