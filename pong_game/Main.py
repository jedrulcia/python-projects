from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(1200, 600)
screen.title("Pong")

left_paddle = Paddle(-570)
right_paddle = Paddle(570)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

while (ball.game_is_on):
    ball.move(left_paddle, right_paddle, scoreboard)
    screen.update()

screen.exitonclick()
