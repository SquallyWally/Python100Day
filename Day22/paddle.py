from turtle import Turtle

# move by 20 pixel

WIDTH = 5
HEIGHT = 1
SHAPE = "square"
COLOR = "white"


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
