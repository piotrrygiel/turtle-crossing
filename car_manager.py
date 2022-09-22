from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=300 + start_x, y=random.randint(-250, 250))

    def move(self, multiplier):
        self.goto(x=self.xcor() - STARTING_MOVE_DISTANCE - multiplier * MOVE_INCREMENT, y=self.ycor())
