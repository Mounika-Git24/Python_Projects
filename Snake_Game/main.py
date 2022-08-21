from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)
# screen.addshape("snakecry.gif")


# turtles = []
# for _ in range(3):
#     t = Turtle(shape="square")
#     t.color("white")
#     turtles.append(t)
#
# turtles[1].goto(20, 0)
# turtles[2].goto(40, 0)
# positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#
# game_on = True
# while game_on:
#     screen.update()
#     time.sleep(0.1)
#     for i in range(len(segments) - 1, 0, -1):
#         pos = segments[i-1].pos()
#         segments[i].goto(pos)
#     segments[0].forward(20)
#     segments[0].left(90)
#

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall.
    if (snake.head.xcor() > 290) or (snake.head.ycor() > 290) or \
            (snake.head.xcor() < -300) or (snake.head.ycor() < -290):
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()

    # increase speed based on the score
    if scoreboard.score > 10:
        snake.head.speed("normal")
    elif scoreboard.score > 20:
        snake.head.speed("fast")
    else:
        snake.head.speed("fastest")

screen.exitonclick()
