# import random
# import colorgram
#
# rgb_kleuren = []
# kleuren = colorgram.extract('image.jpg', 35)
#
# """To get all colors"""
# for kleur in kleuren:
#     r = kleur.rgb.r
#     g = kleur.rgb.g
#     b = kleur.rgb.b
#
#     rgb_kleuren = (r, g, b)
#     #print(rgb_kleuren)

import turtle as t
import random

t.colormode(255)

kleur_lijst = [(226, 231, 237), (59, 106, 147), (223, 234, 230), (224, 201, 111), (235, 227, 207), (133, 84, 59),
               (221, 144, 68), (195, 145, 171), (142, 177, 202), (237, 224, 233), (139, 80, 104), (212, 92, 65),
               (69, 107, 90), (187, 80, 119), (133, 181, 135), (129, 135, 75), (64, 156, 93), (45, 156, 191),
               (183, 191, 201), (217, 176, 191), (20, 61, 96), (19, 68, 114), (117, 122, 148), (231, 175, 164),
               (171, 204, 183), (150, 209, 218), (53, 72, 66), (79, 66, 46), (105, 52, 46), (71, 55, 42), (47, 66, 64),
               (99, 45, 59),
               ]

turtuga = t.Turtle()
turtuga.up()
turtuga.hideturtle()
turtuga.setheading(225)
turtuga.forward(300)
turtuga.setheading(0)

aantal = 100

for count in range(1, aantal):
    turtuga.dot(20, random.choice(kleur_lijst))
    turtuga.forward(50)

    if count % 10 == 0:  # 10, 20,30 etc
        turtuga.setheading(90)
        turtuga.forward(50)
        turtuga.setheading(180)
        turtuga.forward(500)
        turtuga.setheading(0)

screen = t.Screen()
screen.exitonclick()
