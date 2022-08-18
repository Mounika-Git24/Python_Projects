from turtle import Turtle, Screen
import random

screen = Screen()

# Setting screen size to 500px X 500px
screen.setup(width=500, height=500)

# List to add Turtle instances or turtles
turtles = []

y_positions = [-200, -100, 0, 100, 200]
colors = ["brown", "DarkCyan", "green", "HotPink", "navy"]
is_end = False

# taking input from the user
user_input = screen.textinput(title="Betting",
                              prompt="Which turtle will be the winner? "
                                     "Enter color ('brown', 'DarkCyan', 'green', 'HotPink', 'navy'): ")

# Here 5 denotes the number of turtles
for x in range(5):
    # creating Turtle objects
    turtle = Turtle(shape="turtle")

    # Prevents the turtle to do not draw anything
    turtle.penup()

    # stretches the size of the turtle
    turtle.turtlesize(stretch_len=1.8, stretch_wid=1.8)

    # sets the color
    turtle.color(colors[x])

    # move the turtle to the given position
    turtle.goto(-230, y_positions[x])

    # adds new turtles to the list
    turtles.append(turtle)

while not is_end:
    for t in turtles:

        # checks if the turtle cross the end line or winning line
        if t.xcor() > 200:

            # get the color of the winner turtle
            winner = t.pencolor()

            # stops the race
            is_end = True

            # checks if the user entered correct turtle color
            if winner == user_input:
                print(f"You've win!! {winner} turtle is the winner.")
            else:
                print(f"You've lost!! {winner} turtle is the winner.")

            # writes "WINNER" at the winner turtle on the screen
            t.write("WINNER", False, "right", font=('Arial', 20, 'bold'))

        # make the turtle to move forward
        t.forward(random.randint(0, 10))

screen.exitonclick()
