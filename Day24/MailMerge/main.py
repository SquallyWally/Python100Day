PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt", "r") as namen_bestand:
    # for each name in invited_names.txt
    namen = namen_bestand.readlines()

    # Replace the [name] placeholder with the actual name.
    with open("Input/Letters/starting_letter.txt") as letter:
        lines = letter.read()

        for naam in namen:
            naam_strip = naam.strip() #removes crlf, only name
            replaceName = lines.replace(PLACEHOLDER, naam_strip)
            # Save the letters in the folder "ReadyToSend".
            with open(f"Output/ReadyToSend/letter_for_{naam_strip}.txt", "w") as new_letter:
                new_letter.write(replaceName)
