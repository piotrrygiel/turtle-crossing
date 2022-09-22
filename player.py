from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(x=0, y=self.ycor() + MOVE_DISTANCE)

    def finish(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
