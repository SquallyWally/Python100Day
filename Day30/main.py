# # with open("a_file.txt") as file:
# #     file.read()
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Donkey")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     # make own exception with raise
#     raise KeyError("Oh shit")4

hoogte = float(input("Hoogte: "))
gewicht = float(input("gewicht: "))

if hoogte > 3:
    raise ValueError("een persoon die hoger is dan 3 meter?")

bmi = gewicht / hoogte ** 2
print(bmi)
