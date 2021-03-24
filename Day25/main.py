import pandas as pd

# Make csv that has fur, color and count ( dus 3)

data = pd.read_csv("squirrel_data.csv")

# count Grey
# maandag = weer[weer.day == "Monday"]
grijs = data[data["Primary Fur Color"] == "Gray"]
rood = data[data["Primary Fur Color"] == "Cinnamon"]
zwart = data[data["Primary Fur Color"] == "Black"]

print(len(grijs))
print(len(rood))
print(len(zwart))

data_dict = {
    "Fur Kleur": ["grijs", "rood", "zwart"],
    "Aantal": [len(grijs), len(rood), len(zwart)]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
# print(grijs.value_counts())
