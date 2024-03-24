from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while (game_is_on == True):
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.head.distance(food) < 15):
        scoreboard.score += 1
        scoreboard.refresh_score()
        snake.extend_snake()
        food.respawn()
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x >= 300 or head_x <= -300 or head_y >= 300 or head_y <= -300:
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()