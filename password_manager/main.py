import random
import pyperclip
from tkinter import *
from tkinter import messagebox

GREEN = "#1A4D2E"
FONT = "Verdana"


def add_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            pyperclip.copy(password)


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    new_password = "".join(password_list)

    password_entry.insert(0, new_password)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white", padx=10, pady=10)
website_label.config(font=(FONT, 10))
website_label.grid(row=1, column=0)

website_entry = Entry(width=42, highlightthickness=1, font=(FONT, 8))
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white", padx=10, pady=10)
email_label.config(font=(FONT, 10))
email_label.grid(row=2, column=0)

email_entry = Entry(width=42, highlightthickness=1, font=(FONT, 8))
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "xyz@gmail.com")

password_label = Label(text="Password:", bg="white", padx=10, pady=10)
password_label.config(font=(FONT, 10))
password_label.grid(row=3, column=0)

password_entry = Entry(width=26, highlightthickness=1, font=(FONT, 8))
password_entry.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", bg=GREEN, fg="white", activebackground=GREEN, relief=FLAT,
                       command=generate_password)
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=41, bg=GREEN, fg="white", activebackground=GREEN, relief=FLAT, command=add_to_file)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
