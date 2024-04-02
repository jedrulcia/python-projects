from turtle import Turtle


class State(Turtle):
    def __init__(self, name_of_state, x_cord, y_cord):
        super().__init__()
        print(f"{x_cord}, {y_cord}, {name_of_state}")
        self.hideturtle()
        self.penup()
        self.goto(x_cord, y_cord)
        self.write(name_of_state)
