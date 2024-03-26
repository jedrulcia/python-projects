from turtle import Turtle

MAX_SCORE = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.x_move = 0.15
        self.y_move = 0.1
        self.game_is_on = True

    def move(self, left_paddle, right_paddle, scoreboard):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if (self.xcor() < -550):
            self.x_move *= -1
            if (self.distance(left_paddle) < 55):
                scoreboard.l_score += 1
                scoreboard.update_score()
            if (scoreboard.l_score == MAX_SCORE):
                self.game_is_on = False
                scoreboard.display_winner("left")
        elif (self.xcor() > 550):
            self.x_move *= -1
            if (self.distance(right_paddle) < 55):
                scoreboard.r_score += 1
                scoreboard.update_score()
            if (scoreboard.r_score == MAX_SCORE):
                self.game_is_on = False
                scoreboard.display_winner("right")
        if (self.ycor() > 280 or self.ycor() < -280):
            self.y_move *= -1

