import turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.create_shapes()

    def create_shapes(self):
        for i in range(1, 9):
            turtle.register_shape(f'{i}.gif')

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = turtle.Turtle()
            num = random.randint(1, 8)
            new_car.shape(f'{num}.gif')
            new_car.penup()
            random_y = random.randint(-280, 280)
            new_car.goto(-350, random_y)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.moving_speed)

    def level_up(self):
        self.moving_speed += MOVE_INCREMENT













