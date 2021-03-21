from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.alle_autos = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def maak_autos(self):
        random_chance = random.randint(1, 6)  # so therw wont be too many cars
        if random_chance == 1:  # maakt ene auto 1/6 keer
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.alle_autos.append(new_car)

    def beweeg_autos(self):
        for auto in self.alle_autos:
            auto.back(self.car_speed)

    def more_speed(self):
        self.car_speed += MOVE_INCREMENT
