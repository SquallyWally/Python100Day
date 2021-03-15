import turtle as t

import turtle as t

import heroes
import random

turtuga = t.Turtle()
turtuga.shape("classic")
turtuga.color("DeepSkyBlue4")
t.colormode(255)
print(heroes.gen())

def willekeurig_kleur():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

#random kleur met rgb ( dus met tuples)


"""Teken direhoek naar 11hoek"""
# def teken(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         turtuga.forward(100)
#         turtuga.right(angle)
#
#
# for x in range(3, 11):
#     turtuga.color(random.choice(kleur))
#     teken(x)

'''Random walk'''

posities = [90, 180, 270, 0]

turtuga.speed("fastest")
for _ in range(400):
    turtuga.pensize(10)
    turtuga.forward(20)
    turtuga.right(random.choice(posities))
    turtuga.color(willekeurig_kleur())
    turtuga.forward(20)
# turtuga.setposition(1,0)
# for _ in range(10):
#    turtuga.down()
#   turtuga.forward(20)
#  turtuga.up()
# turtuga.forward(20)

screen = t.Screen()
screen.exitonclick()
