from turtle import Screen
from player import Player
from cars import Cars
import time
import random
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle crossing")

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")

game_is_on = True
while (game_is_on):
    number = random.randint(0, 20)
    if (number == 20):
        cars.create_car()
    if (player.ycor() > 270):
        scoreboard.score += 1
        scoreboard.refresh_score()
        player.goto(0, -280)
        cars.remove_cars()
        cars.car_speed *= 1.25
    game_is_on = cars.check_collision(player)
    cars.move()
    screen.update()
    time.sleep(0.01)

scoreboard.game_over()
screen.exitonclick()








