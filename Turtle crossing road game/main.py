from turtle import Turtle, Screen
from player import Player
import time
from carmanager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.listen()
sleep_time = 0.2
screen.setup(width=600, height=600)
player = Player()
carmanager = CarManager()
scoreboard = ScoreBoard()
screen.onkeypress(key="Up",fun=player.move_player)

is_game_on = True
while is_game_on:
    carmanager.create_car()
    carmanager.move_car()

    for cars in carmanager.carlist:
        if player.distance(cars) < 25:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() > 250:
        scoreboard.update_score()
        player.reset()
        if sleep_time > 0.01:
            sleep_time *= 0.7
            player.increase_speed()


    time.sleep(sleep_time)
    screen.update()


screen.exitonclick()