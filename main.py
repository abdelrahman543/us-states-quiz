from turtle import Turtle , Screen
import pandas

data = pandas.read_csv("50_states.csv")
screen = Screen()
screen.title("Us states game")
image = "blank_states_img.gif"
screen.addshape(image)
Turtle(image)
states = data.state.tolist()
# or u can use ["state"].value
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct" , prompt="guess a state").title()
    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer in states:
        guessed_states.append(answer)
        timmy = Turtle()
        timmy.penup()
        timmy.hideturtle()
        location = data[data.state == answer]
        timmy.goto(location.x.item() , location.y.item())
        timmy.write(answer)

