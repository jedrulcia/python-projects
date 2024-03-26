from turtle import Turtle

MOVE_DISTANCE = 1


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position_x, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
