from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Data/words_list.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    flash_card.itemconfig(card_title, text="Word", fill="black")
    flash_card.itemconfig(card_word, text=current_word['word'], font=("Ariel", 50, "bold"), fill="black")
    flash_card.itemconfig(card_pro, text=current_word['pronunciation'], state="normal")
    flash_card.itemconfig(card_background, image=front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(card_title, text="Meaning", fill="white")
    flash_card.itemconfig(card_word, text=current_word["meaning"], fill="white",
                          font=("Ariel", 20, "bold"), justify="center", width=600)
    flash_card.itemconfig(card_pro, state="hidden")
    flash_card.itemconfig(card_background, image=back)


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")

flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = flash_card.create_image(400, 263, image=front)
card_title = flash_card.create_text(400, 100, text="Title", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(400, 263, text="Text", font=("Ariel", 50, "bold"))
card_pro = flash_card.create_text(400, 320, text="Pronunciation", font=("Ariel", 20, "bold"), fill="gray")
flash_card.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(relief=FLAT, image=wrong_img, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, relief=FLAT, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)


next_card()
window.mainloop()
