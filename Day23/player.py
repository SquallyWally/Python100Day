from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(STARTING_POSITION)

    def beweeg(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # of self.forward(MOVE_DISTANCE)

    def reached_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
