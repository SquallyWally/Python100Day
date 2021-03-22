from turtle import Turtle
import random


class Food(Turtle):

    # Food inherit from Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
