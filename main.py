import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
spawn_delay = 20
speed_multiplier = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager = CarManager(spawn_delay)
    cars.append(car_manager)
    spawn_delay += 20

    for car in cars:
        car.move(speed_multiplier)
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.finish()
        speed_multiplier += 1
        scoreboard.update()

screen.exitonclick()
