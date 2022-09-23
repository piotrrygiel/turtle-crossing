from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.left_cars = []
        self.right_cars = []
        self.reserve_cars = []

    def spawn_car(self, start_x):
        print(len(self.right_cars))
        if self.reserve_cars:
            new_car = self.reserve_cars.pop()
        else:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
        new_car.goto(x=300 + start_x, y=random.randrange(-240, 0, 30))
        self.right_cars.append(new_car)
        another_car = new_car.clone()
        another_car.goto(x=-300 - start_x, y=random.randrange(0, 240, 30))
        self.left_cars.append(another_car)

    def move(self, multiplier):
        for car in self.right_cars:
            car.goto(x=car.xcor() - STARTING_MOVE_DISTANCE - multiplier * MOVE_INCREMENT, y=car.ycor())
            if car.xcor() < -320:
                self.right_cars.remove(car)
                self.reserve_cars.append(car)
        for car in self.left_cars:
            car.goto(x=car.xcor() + STARTING_MOVE_DISTANCE + multiplier * MOVE_INCREMENT, y=car.ycor())
