import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from environment import Environment

spawn_delay = 40
speed_multiplier = 0

screen = Screen()
screen.register_shape("little_turtle.gif")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player("little_turtle.gif")
scoreboard = Scoreboard()
car_manager = CarManager()
environment = Environment()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.spawn_car(spawn_delay)
    spawn_delay += 40
    car_manager.move(speed_multiplier)

    for car in car_manager.right_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    for car in car_manager.left_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.finish()
        speed_multiplier += 1
        scoreboard.update()

screen.exitonclick()
