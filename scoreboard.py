from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-210, y=260)
        self.update()

    def update(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)
