from turtle import Turtle
from setup import Screen_height,Screen_width


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.pu()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 270:
            self.goto(self.xcor(),self.ycor()+10)

    def move_down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(),self.ycor()-10)


