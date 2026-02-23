from turtle import Turtle, Screen
import pandas
import time

turtle = Turtle()
writer = Turtle()
screen = Screen()
screen.title("u.s.a")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0
turtle.penup()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
STATE_DATA = data.state.to_list()




map_stage = []
while len(map_stage) < 50:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="what's another name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in STATE_DATA if state not in map_stage]
        # for state in STATE_DATA:
        #     if state not in map_stage:
        #         missing_states.append(state)
        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv("Missing_states to learn.csv")
        break
    if answer_state in STATE_DATA:
        map_stage.append(answer_state)
        correct += 1
        map_data = data[data.state == answer_state]
        x_cor = map_data.x.item()
        y_cor = map_data.y.item()
        writer.goto(x_cor, y_cor)
        writer.write(answer_state)




