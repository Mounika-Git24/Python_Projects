from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-280, 310)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center",
                   font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "bold"))




