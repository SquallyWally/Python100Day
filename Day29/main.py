from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letter_list + number_list + symbols_list
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = user_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oopsie daisy", message="Something wrong fam")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"these are the details:\nEmail:{email}\nPassword: {password}\nIs ok?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} ||| {email} ||| {password}\n")
                # Empty the fields
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
foto = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=foto)
canvas.grid(column=1, row=0)

website_Label = Label(text="Website:")
website_Label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()  # focused on tht Entry
website_entry.grid(column=1, row=1, columnspan=2)
# website_entry.insert(0,string=input())

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, string="milo@outlook.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
