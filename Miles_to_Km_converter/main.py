from tkinter import *


def calculate():
    into_km = float(user_input.get()) * 1.60934
    result.config(text=f"{into_km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20, background="white")

user_input = Entry(font=("Arial", 15), background="white", foreground="navy", justify="center", width=15)
user_input.grid(column=1, row=0)


miles = Label(text="Miles", font=("Arial", 15))
miles.config(padx=10, pady=10, background="white")
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 15))
equal_to.config(padx=10, pady=10, background="white")
equal_to.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 15))
result.config(padx=10, pady=10, background="white", foreground="navy")
result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 15))
km.config(padx=10, pady=10, background="white")
km.grid(column=2, row=1)

button = Button(text="Calculate", font=("Arial", 15), command=calculate)
button.config(background="pink")
button.grid(column=1, row=2)

window.mainloop()
