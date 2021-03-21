import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(key="w", fun=player.beweeg)

car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.maak_autos()
    car.beweeg_autos()

    for auto in car.alle_autos:
        if auto.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.reached_finish():
        player.reset_position()
        car.more_speed()
        score.level_up()


screen.exitonclick()
