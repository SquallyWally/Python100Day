import turtle as t
import random

turtuga = t.Turtle()

t.colormode(255)
turtuga.speed("fastest")

def willekeurig_kleur():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    kleur = (r, g, b)
    return kleur

def teken(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtuga.circle(100)
        turtuga.color(willekeurig_kleur())
        turtuga.setheading(turtuga.heading()+size_of_gap)


teken(5)
screen = t.Screen()
screen.exitonclick()

