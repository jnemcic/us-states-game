from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.addshape(image)

turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
correct_guesses = 0

while len(guessed_states) < 50:
    guess = screen.textinput(f"{correct_guesses}/50 States correct ", "What's another state name? ").title()
    if guess == "Exit":
        forgotten_states = [state for state in all_states if state not in guessed_states]
        forgotten_states_df = pandas.DataFrame(forgotten_states)
        forgotten_states_df.to_csv("forgotten_states.csv")
        forgotten_states_df.row
        break
    else:
        if guess in all_states:
            guess_entry = data[data.state == guess]
            turtle.goto(int(guess_entry.x), int(guess_entry.y))
            turtle.write(f"{guess_entry.state.item()}", font=("Verdana", 12, "normal"))
            correct_guesses += 1
            guessed_states.append(guess)
