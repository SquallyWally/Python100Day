from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_level()

    def show_level(self):
        self.goto(y=260, x=-200)
        self.write(f"Level: {self.level} ", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



