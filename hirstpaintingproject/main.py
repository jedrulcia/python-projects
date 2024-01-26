import colorgram
import turtle as t
import random

def extract_colors():
    colors = colorgram.extract("image.jpg", 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


rgb_colors = extract_colors()

timmy = t.Turtle()
timmy.width(10)
t.colormode(255)
timmy.speed(30)


x = 0
for _ in range(13):
    timmy.teleport(-300,-300 + x)
    x += 50
    for _ in range(13):
        timmy.color(random.choice(rgb_colors))
        timmy.dot()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


screen = t.Screen()
screen.exitonclick()