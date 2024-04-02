import turtle, pandas
from guessed_states import State

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.setup(width=750,height=520)
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_cords = data["x"].to_list()
y_cords = data["y"].to_list()

game_is_on = True
while len(states) != 0:
    guess = screen.textinput(title=f"{50-len(states)}/50 States Correct", prompt="What's another state's name?")
    for index, state in enumerate(states):
        if guess.lower() == state.lower():
            State(states[index], x_cords[index], y_cords[index])
            del states[index]
            del x_cords[index]
            del y_cords[index]
    if (guess == "exit"):
        break

states_to_learn = pandas.DataFrame(states)
states_to_learn.to_csv("states_to_learn.csv")

