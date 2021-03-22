from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
slang = Snake()
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(slang.up, "Up")
scr.onkey(slang.down, "Down")
scr.onkey(slang.left, "Left")
scr.onkey(slang.right, "Right")

game_is_on = True

'''Moves snake'''
while game_is_on:
    """Only being delayed when all 3 snakes are moved except per snake"""
    scr.update()
    time.sleep(0.1)
    slang.beweeg()

    # Detect collision with food, 15 is the best distance after tweaking
    if slang.head.distance(food) < 15:
        print("GOLOS")
        food.refresh()
        slang.extend()
        score.increase_score()

    # detect collision with wall
    if slang.head.xcor() > 280 or slang.head.xcor() < -280 or slang.head.ycor() > 280 or slang.head.ycor() < -280:
        # game_is_on = False
        #  score.game_over()
        score.reset()
        slang.reset()

    # detect collision with tail with slicing
    for this_slang in slang.slangen[1:]:
        # so you dont start at once with a Game over screen
        if slang.head.distance(this_slang) < 10:
            score.reset()
            slang.reset()
    # game_is_on = False
    #  score.game_over()

scr.exitonclick()
