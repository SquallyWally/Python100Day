from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("Murica States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtuga = Turtle()
turtuga.shape(image)

gegokte_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(gegokte_states) < 50:
    antwoord_state = screen.textinput(title=f"{len(gegokte_states)}/50 States correct", prompt="State's name?")
    print(antwoord_state)

    if antwoord_state == "Exit":
        # missing_states = []
        # for element in all_states:
        #     if element not in gegokte_states:
        #         missing_states.append(element)
        missing_states = [element for element in all_states if element not in gegokte_states]
        print(missing_states)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if antwoord_state in all_states:
        gegokte_states.append(antwoord_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == antwoord_state]  # when the state is correct
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(antwoord_state)  # of t.write(state_data.state.item())

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
