import tkinter
import random
import string
import pyperclip
import json
from tkinter import messagebox

all_characters = string.ascii_letters + string.digits + string.punctuation


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    for i in range(20):
        password += random.choice(all_characters)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE CREDENTIALS ------------------------------- #
def add_credentials():
    website = website_input.get().lower()
    username = username_input.get()
    password = password_input.get()

    newdata = {
        "Username": username,
        "Password": password
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[website] = newdata
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo(title="Credentials saved",
                            message=f"Credentials successfully saved\n"
                                    f"Website: {website}\n"
                                    f"Username: {username}\n"
                                    f"Password: {password}.")

        website_input.delete(0)
        password_input.delete(0)


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credentials():
    website = website_input.get().lower()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            credentials = data[website]
            messagebox.showinfo(title=f"Your credentials",
                                message=f"Website: {website}\n"
                                        f"Username: {credentials["Username"]}\n"
                                        f"Password: {credentials["Password"]}")
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title=f"Credentials error", message="You haven't got any credentials for this webiste")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)

username_label = tkinter.Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

# Inputs
website_input = tkinter.Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = tkinter.Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "user@gmail.com")

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
search_button = tkinter.Button(text="Search", width=13, command=search_credentials)
search_button.grid(row=1, column=2)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=add_credentials)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
