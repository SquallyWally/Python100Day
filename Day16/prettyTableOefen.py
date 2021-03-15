from turtle import *

# turtuga = Turtle()
# turtuga.shape("turtle")
# turtuga.color('blue')
# my_screen = Screen()
#
# turtuga.fd(100)
##show turtle screen
# my_screen.exitonclick()
#
#
# def draw_star():
#    color('red', 'yellow')
#    begin_fill()
#    while True:
#        forward(200)
#        left(170)
#        if abs(pos()) >= 1:
#            continue
#        break
#    end_fill()
#    done()
#

# draw_star()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]

table.add_rows(
    [
        ["Bulbasaur", "Grass"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"

print(table)
