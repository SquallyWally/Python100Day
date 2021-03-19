from turtle import Turtle

WIDTH = 0.7
HEIGHT = 0.7
X_POS = 0
Y_POS = 0


# goes up right
# After refresh, ball goes back to (0.0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("purple")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)

        # for bouncing
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        # trajectory will reverse
        self.y_move *= -1
        #self.move_speed *= 0.9 , anders gaat die stotteren

    def bounce_x(self):
        # trajectory will reverse
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
