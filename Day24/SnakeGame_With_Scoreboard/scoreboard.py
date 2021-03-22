from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
                "/home/milo/PycharmProjects/Python100Day/Day24/SnakeGame_With_Scoreboard/data.txt") as data:  # change to just "data.txt"
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/home/milo/PycharmProjects/Python100Day/Day24/SnakeGame_With_Scoreboard/data.txt",
                      mode="w") as data:  # change to just "data.txt"
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

# def save_score(self):

# def game_over(self):
#     self.goto(0, 0)
#     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
