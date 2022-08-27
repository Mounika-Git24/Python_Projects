from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgpic('road.png')
screen.setup(700, 700)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            score_board.game_over()
            game_on = False

    # next level
    if player.ycor() > 320:
        player.go_to_start()
        score_board.update_level()
        car_manager.level_up()


screen.exitonclick()
