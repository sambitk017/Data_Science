
################### Setting up the Screen ###############################


import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):     this cpommented out code give the location or cordinates of the click
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()
guess_states = []

while len(guess_states) < 50:
    answer_data = screen.textinput(title=f"{len(guess_states)}", prompt="whats the other state names").title()  # this creates a pop-up
    print(answer_data)  #for the screen to show the question in prompt and the answer

    if answer_data in all_states:
        guess_states.append(answer_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()               # thi if statment checks and write the answer on the screen at the place of coordinates
        state_cor = data[data["state"] == answer_data]
        t.goto(int(state_cor["x"]), int(state_cor["y"]))
        t.write(state_cor["state"].item())



screen.exitonclick()













