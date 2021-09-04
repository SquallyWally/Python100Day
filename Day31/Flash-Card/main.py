import random
from tkinter import *

import pandas

to_learn = {}
current_card = {}

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/italian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Italiaans", fill="black")
    canvas.itemconfig(card_word, text=current_card["Italiaans"], fill="black")
    canvas.itemconfig(card_background, image=front_card)  # reset the card back
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Nederlands", fill="white")
    canvas.itemconfig(card_word, text=current_card["Nederlands"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  # wont keep adding a new index
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")
# timer
# 3 seconds
flip_timer = window.after(3000, func=flip_card)

my_image_right = PhotoImage(file="images/right.png")
my_image_wrong = PhotoImage(file="images/wrong.png")
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(highlightthickness=0, bg="#B1DDC6")

right_btn = Button(image=my_image_right, highlightthickness=0, command=is_known)
wrong_btn = Button(image=my_image_wrong, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

next_card()  # generate next card

window.mainloop()
