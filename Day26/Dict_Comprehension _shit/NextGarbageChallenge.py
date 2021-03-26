# create dict that takes each word in the given sentence and calc number of letters per word

# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
splitted_words = sentence.split()
result = {element: len(element) for element in splitted_words}
print(result)

####
# Create dict that takes each temp in degrees Celsius and converts it into Murica Celsius(F)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: ((temp * 9 / 5) + 32) for (day, temp) in weather_c.items()}
print(weather_f)


#for(index,row) in dateframe.iterrows():
    #print(row.name) or just a normal if loop