from turtle import Turtle
STARTING_POSITION = (0, -330)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.seth(90)
        self.shapesize(1.5, 1.5)
        self.penup()
        self.go_to_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)



