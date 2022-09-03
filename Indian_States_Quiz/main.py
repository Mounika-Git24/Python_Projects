"""
------python coordinate locator-----

def mouse_click(x, y):
    print(x, y)


turtle.onscreenclick(mouse_click)
turtle.mainloop()"""

from turtle import Turtle, Screen
import pandas

# screen setup
screen = Screen()
screen.title("Indian States Game")
screen.setup(600, 600)
screen.bgpic("india.gif")

t = Turtle()
t.penup()
t.hideturtle()
t.shapesize(0.1, 0.1)
t.shape("circle")
t.color("purple")

data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 37:
    guess = len(guessed_states)
    state = screen.textinput(f"{guess}/36 states guessed correctly.", "What's another state name?").title()

    if state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if state in all_states:
        guessed_states.append(state)
        t.goto(data[data["state"] == state]["x"].item(), data[data["state"] == state]["y"].item())
        t.stamp()
        t.write(state, align="center", font=("Ariel", 8, "bold"))
