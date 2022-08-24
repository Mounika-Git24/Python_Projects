from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


game_on = True


def exit_game():
    global game_on
    game_on = False


# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

# controls turtle animation
screen.tracer(0)

# adding left and right paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# adding dashed line in middle
line = Turtle()
line.hideturtle()
line.penup()
line.goto(0, 300)
line.left(270)
line.pendown()
for _ in range(56):
    line.color("white")
    line.forward(5)
    line.color("black")
    line.forward(5)

# adding comment for the user
line.penup()
line.forward(20)
line.color("gray")
line.write("Press Enter to Exit", align="center", font=('Arial', 15, 'normal'))

# adding ball
ball = Ball()

# key listener
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(exit_game, "Return")

# adding scores
score = Scoreboard()

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.bounce_x()
#
    # detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()
#
    # detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
