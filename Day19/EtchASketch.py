from turtle import Turtle, Screen

turtuga = Turtle()
screen = Screen()


def beweeg_naar_voren():
    turtuga.forward(10)


def beweeg_naar_achter():
    turtuga.backward(10)


def beweeg_naar_rechts():
    turtuga.right(10)


def beweeg_naar_links():
    turtuga.left(10)


def clear():
    turtuga.reset()
    turtuga.penup()
    turtuga.home()
    turtuga.pendown()


screen.listen()
screen.onkey(key="w", fun=beweeg_naar_voren)
screen.onkey(key="s", fun=beweeg_naar_achter)
screen.onkey(key="a", fun=beweeg_naar_links)
screen.onkey(key="d", fun=beweeg_naar_rechts)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
