from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.speed(1)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            position = self.segments[i - 1].pos()
            self.segments[i].goto(position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.seth(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.seth(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.seth(RIGHT)
