from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, -120)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=FONT)
