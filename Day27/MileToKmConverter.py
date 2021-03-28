from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=220, height=30)


def calculate_clicked():
    # new_km = score.getint()
    input = entry.get()
    score_km = round(int(input) * 1.6)

    print(score_km)
    score.config(text=score_km)


score = Label(text="0")
equalLabel = Label(text="is equal to")
kmLabel = Label(text="Km")
entry = Entry(width=10)
entry.insert(END, string="0")
milesLabel = Label(text="Miles")
calcButton = Button(text="Calculate", command=calculate_clicked)

equalLabel.grid(column=0, row=2)
score.grid(column=1, row=2)
kmLabel.grid(column=2, row=2)
entry.grid(column=1, row=1)
milesLabel.grid(column=2, row=1)
calcButton.grid(column=1, row=3)

window.mainloop()
