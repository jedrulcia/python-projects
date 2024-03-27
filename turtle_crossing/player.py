from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.speed("normal")
        self.turtlesize(1)
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 5)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 5)






