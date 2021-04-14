# Author: Milo K
# Lmao

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = user_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oopsie daisy", message="Something wrong fam")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data
            data.update(new_data)
            # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                if __debug__:
                    print(data)
                else:
                    print("Garbage Donkey Ginger")
        finally:
            # Empty the fields
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ------------------------ SEARCH FOR SAVES --------------------------- #
def find_password():
    site = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oopsie daisy", message="Something wrong fam and no data found")
    else:
        if site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=f"{site}",
                                message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oopsie daisy", message=f"no details for {site} exists")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_Label = Label(text="Website:")
website_Label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.focus()  # focused on tht Entry
website_entry.grid(column=1, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=40)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, string="test@outlook.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
