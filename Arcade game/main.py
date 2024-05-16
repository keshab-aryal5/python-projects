from setup import Screen_height,Screen_width,Screen_bgcolor
import random
from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard
def make_mid_line():
    mid_line = Turtle()
    mid_line.ht()
    mid_line.pu()
    mid_line.goto(0, Screen_height // 2)
    mid_line.color("white")
    mid_line.setheading(270)
    mid_line.width(5)
    while mid_line.ycor() > -(Screen_height // 2):
        mid_line.pd()
        mid_line.fd(20)
        mid_line.pu()
        mid_line.fd(20)


is_game_on = True
screen = Screen()
screen.tracer(0)
screen.title("Arcade game")

screen.bgcolor(Screen_bgcolor)
l_paddle = Paddle((-360,0))
r_paddle = Paddle((350,0))

ball = Ball()
l_scoreboard = ScoreBoard((-170,200))
r_scoreboard = ScoreBoard((150,200))

make_mid_line()
screen.listen()

screen.onkeypress(key="Up",fun=r_paddle.move_up)
screen.onkeypress(key="Down",fun=r_paddle.move_down)
screen.onkeypress(key="w",fun=l_paddle.move_up)
screen.onkeypress(key="s",fun=l_paddle.move_down)
while is_game_on:
    ball.move_ball()
    ball.collision_with_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() == 330:
        ball.collision_with_paddle()

    elif ball.distance(l_paddle) < 50 and ball.xcor() == -340:
        ball.collision_with_paddle()

    elif ball.xcor() > 330:
        l_scoreboard.update_score()
        ball.reset_ball()

    elif ball.xcor() < -340:
        r_scoreboard.update_score()
        ball.reset_ball()

    screen.update()
    time.sleep(ball.move_speed)
screen.exitonclick()
