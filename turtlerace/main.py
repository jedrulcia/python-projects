from turtle import *
import random


screen = Screen()
screen.setup(500, 350)
colors = ["blue", "orange", "purple", "red", "yellow", "green"]
y_positions = [125, 75, 25, -25, -75, -125]
turtles = []
is_race_on = False

for turtle_index in range(6):
    timmy = Turtle("turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(-230, y_positions[turtle_index])
    turtles.append(timmy)


user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
if (user_bet):
    is_race_on = True

while (is_race_on):
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False
            if (user_bet == winner):
                print("You have made a right guess!")
            else:
                print("You haven't made a right guess :(")
            print(f"{winner} turtle has won!")



screen.exitonclick()

