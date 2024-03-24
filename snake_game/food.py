from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("yellow")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        random_x = random.randint(-14, 14)
        random_y = random.randint(-14, 14)
        self.goto(random_x * 20, random_y * 20)
