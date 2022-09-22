from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def spawn_car(self, start_x):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300 + start_x, y=random.randrange(-240, 240, 30))
        self.all_cars.append(new_car)

    def move(self, multiplier):
        for car in self.all_cars:
            car.goto(x=car.xcor() - STARTING_MOVE_DISTANCE - multiplier * MOVE_INCREMENT, y=car.ycor())
