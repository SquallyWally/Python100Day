from tkinter import *

window = Tk()
window.title("GUi Donkey Garbage")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
myLabel = Label(text="I am a donkey Label", font=("Arial", 24, "italic"))
myLabel.config(text="Donkeu")
# myLabel.place(x=0, y=0)
myLabel.grid(column=0, row=0)


# Button
def button_clicked():
    print("got clicked donkey")
    new_donkey = input.get()
    myLabel.config(text=new_donkey)
    myLabel.config(text="got clicked donkey")


button = Button(text="Donkeyy", command=button_clicked)
new_button = Button(text="Second_Donkey", command=button_clicked)
button.grid(column=1,row=1)
new_button.grid(column=2,row=0)


# Entry
input = Entry(width=15)
print(input.get())
#input.pack()
input.grid(column=3,row=3)

window.mainloop()  # keeps the window open
