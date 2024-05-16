from turtle import Turtle
from setup import Ball_size,Screen_height,Screen_width
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.make_ball()
        self.choice = [-1,1]
        self.move_speed = 0.1

    def make_ball(self):
        self.color("white")
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.home()

    def move_ball(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def reset_ball(self):
        self.home()
        self.x_move *= -1
        self.y_move *= random.choice(self.choice)

    def collision_with_wall(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.y_move *= -1

    def collision_with_paddle(self):
        self.x_move *= -1
        self.y_move *= random.choice(self.choice)
        self.move_speed *= 0.9







