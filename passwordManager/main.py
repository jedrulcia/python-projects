import tkinter
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
all_characters = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    password = ""
    for i in range(20):
        password+= random.choice(all_characters)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    try:
        file = open("passwords.txt")
    except FileNotFoundError:
        file = open("passwords.txt", "w")
        file.write("WEBSITE | USERNAME | PASSWORD\n")
    with open("passwords.txt", "a") as file:
        file.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)

window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(1, minsize=30)
window.grid_rowconfigure(2, minsize=30)
window.grid_rowconfigure(3, minsize=30)
window.grid_rowconfigure(4, minsize=30)

canvas = tkinter.Canvas(width=200, height=200)
canvas.grid(row=0, column =3)

photo = tkinter.PhotoImage(file="logo.png")

canvas.create_image(100,100, image=photo)

website_label = tkinter.Label(text="Website: ")
website_label.grid(row =1, column=2)

username_label = tkinter.Label(text="Email/Username: ")
username_label.grid(row = 2, column = 2)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row = 3, column = 2)

website_input = tkinter.Entry(width=50)
website_input.grid(row = 1, column = 3, columnspan =2, sticky="ew")

username_input = tkinter.Entry()
username_input.grid(row = 2, column = 3, columnspan =2, sticky="ew")

password_container = tkinter.Frame()
password_container.grid(row=3, column =3, columnspan=2, sticky="ew")

password_input = tkinter.Entry(password_container)
password_input.pack(side="left", expand=True, padx=(0, 10))

generate_password_button = tkinter.Button(password_container, text="Generate Password", command=generate_password)
generate_password_button.pack(side="right", expand=True)

add_button = tkinter.Button(text="Add", command=add_password)
add_button.grid(row = 4, column = 3, columnspan =2, sticky="ew")

window.mainloop()