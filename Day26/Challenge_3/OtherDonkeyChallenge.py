# new_list = [new_item for item in list]
with open("file1.txt") as file1:
    data1 = file1.readlines()

with open("file2.txt") as file2:
    data2 = file2.readlines()

results = [int(item) for item in data1 if item in data2]

print(results)