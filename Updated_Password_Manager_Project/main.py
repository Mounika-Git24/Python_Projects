import random
import pyperclip
from tkinter import *
from tkinter import messagebox
import json

GREEN = "#3D8361"
FONT = "Verdana"


def add_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
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


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="error", message="No Data File Found.")
    else:
        if website in data:
            website_data = data[website]
            messagebox.showinfo(title=website,
                                message=f"Email: {website_data['email']} \nPassword: {website_data['password']}")
        else:
            messagebox.showwarning(title=website, message=f"No details for {website} exists.")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


# Labels

website_label = Label(text="Website:", bg="white", padx=10, pady=10)
website_label.config(font=(FONT, 10))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white", padx=10, pady=10)
email_label.config(font=(FONT, 10))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white", padx=10, pady=10)
password_label.config(font=(FONT, 10))
password_label.grid(row=3, column=0)


# Entries

website_entry = Entry(width=22, highlightthickness=2, font=(FONT, 9))
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=36, highlightthickness=2, font=(FONT, 9))
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "xyz@gmail.com")

password_entry = Entry(width=22, highlightthickness=2, font=(FONT, 9))
password_entry.grid(row=3, column=1)


# Buttons

search = Button(text="Search", bg=GREEN, fg="white", activebackground=GREEN, relief=RAISED, width=14,
                command=find_password)
search.grid(row=1, column=2)

generate_pass = Button(text="Generate Password", bg=GREEN, fg="white", activebackground=GREEN, relief=RAISED,
                       command=generate_password)
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=40, bg=GREEN, fg="white", activebackground=GREEN, relief=RAISED, command=add_to_file)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
