from tkinter import *
import math

FONT_NAME = "Courier"
RED = "#C21010"
WHITE = "#FFFDE3"
LIGHT_RED = "#E64848"
GREEN = "#CFE8A9"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=LIGHT_RED)
    else:
        count_down(WORK_MIN* 60)
        title.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=20, bg=WHITE)

label = Label(text="Pomodoro", font=("Brush Script MT", 40, "bold"), bg=WHITE, fg=RED, padx=10, pady=20)
label.grid(row=0, column=1)

title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=WHITE, fg=GREEN)
title.grid(row=1, column=1)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=1)

start = Button(text="Start", bg=GREEN, highlightthickness=0, relief=FLAT,
               activebackground=GREEN,command=start_timer)
start.grid(row=3, column=0)

reset = Button(text="Reset", bg=GREEN, highlightthickness=0, relief=FLAT,
               activebackground=GREEN, command=reset_timer)
reset.grid(row=3, column=2)

check_marks = Label(text="", fg="green", bg=WHITE, font=(FONT_NAME, 15))
check_marks.grid(row=4, column=1)

window.mainloop()
