# with open("weather_data.csv") as bestand:
#     data = bestand.readlines()
#
#     print(data)

# import csv
#
# with open("weather_data.csv") as bestand:
#     data = csv.reader(bestand)
#     temps = []
#     for element in data:
#         if element[1] != "temp":
#             temps.append(int(element[1]))
#
#     print(temps)

import pandas as pd

weer = pd.read_csv("weather_data.csv")
# print(type(weer))
# print(weer["temp"])

# weer_dict = weer.to_dict()
# print(weer_dict)
#
# weer_list = weer["temp"].to_list()
# print(weer_list)
#
# print(weer["temp"].mean())
# print(weer["temp"].max())
#
# #Get data in colomns
# print(weer.condition)


# Get row data
# print(weer[weer.day == "Tuesday"])

# Get max
# print(weer[weer.temp == weer.temp.max()])
#
# # Celsius to Fahr (Murica)
# maandag = weer[weer.temp == 24]
# # maandag_temp = int(maandag.temp)
# # maandag_fahr = maandag_temp * 9 / 5 + 32
#  print(maandag.count())
# #
# # # Create Dataframe from Scratch
# # data_dict = {
# #     "gamers": ["Jin", "Xiaoyu", "Eddy"],
# #     "scores": [97, 83, 87]
# # }
# #
# # data_dict_df = pd.DataFrame(data_dict)
# # data_dict_df.to_csv("gamers_data.csv")
# #
# # print(data_dict_df)
