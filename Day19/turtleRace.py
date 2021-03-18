from turtle import Screen, Turtle
import random

is_race_on = False
kleuren = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet donkey", prompt="Pick a turtle color: ")
print(user_bet)

y_pos = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_index in range(0, 6):
    new_turtuga = Turtle(shape="turtle")
    new_turtuga.color(kleuren[turtle_index])
    new_turtuga.penup()
    new_turtuga.goto(x=-460, y=y_pos[turtle_index])
    turtle_list.append(new_turtuga)

if user_bet:
    is_race_on = True

while is_race_on:
    for element in turtle_list:
        if element.xcor() > 460:
            is_race_on = False
            gewonnen_kleur = element.pencolor()
            if gewonnen_kleur == user_bet:
                print(f"You winnah! The winning color was {gewonnen_kleur}")
            else:
                print(f"You LOST! The winning color was {gewonnen_kleur}")

        random_distance = random.randint(0, 10)
        element.forward(random_distance)
screen.exitonclick()
