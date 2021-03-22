with open("my_file") as file:
  #  file.write("\nDekker wekker kek mek")
    content = file.read()
    print(content)

# file.close()  # so it free up the resources, hoeft niet met "with:

with open("wubba", mode="w") as bestand:
    bestand.write("gtrefwklads")