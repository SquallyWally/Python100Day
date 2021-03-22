from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.slangen = []
        self.maakSlang()
        self.head = self.slangen[0]

    def maakSlang(self):
        """Create snake"""
        for positions in START_POS:
            self.add_slang(positions)

    def add_slang(self, positie):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(positie)
        self.slangen.append(snake)

    def extend(self):
        # add anoher snake block
        self.add_slang(self.slangen[-1].position())  # voegt ene nieuwe blok aan het eind, dus -1

    def beweeg(self):
        for snake_num in range(len(self.slangen) - 1, 0, -1):  # start , stop , step
            new_x = self.slangen[snake_num - 1].xcor()
            new_y = self.slangen[snake_num - 1].ycor()
            self.slangen[snake_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)  # so the thingy can move

    #  self.slangen[0].left(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # if check
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for slang in self.slangen:
            slang.goto(1000, 1000) #so old snake goes out of the screen
        self.slangen.clear()
        self.maakSlang()
        self.head = self.slangen[0]
