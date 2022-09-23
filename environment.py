from turtle import Turtle

INCREMENT = 30


class Environment(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=300, y=-255)
        self.draw_lines()

    def draw_lines(self):
        for i in range(17):
            self.goto(x=-300, y=self.ycor())
            self.penup()
            self.goto(x=300, y=self.ycor() + INCREMENT)
            self.pendown()
