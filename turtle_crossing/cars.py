from turtle import Turtle
import random

COLORS = ["red", "blue", "yellow", "green", "orange", "white", "purple"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.car_speed = 1

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        y_cor = random.randint(-280, 280)
        new_car.goto(320, y_cor)
        new_car.speed = 1
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(1 * self.car_speed)

    def remove_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    def check_collision(self, player):
        for car in self.cars:
            if (car.distance(player) < 20):
                return False
        return True
