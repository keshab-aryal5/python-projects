from turtle import Turtle
from setup import Screen_height,Screen_width,Food_size,Food_color
import random


class Food(Turtle):
    def new_food(self):
        self.clear()
        height = Screen_height-50
        width = Screen_width-50
        x = random.randint(-width//2,width//2)
        y = random.randint(-height//2,height//2)
        self.pu()
        self.hideturtle()
        self.shape("circle")
        self.goto(x,y)
        self.speed("fastest")
        self.dot(Food_size,Food_color)

    def get_position(self):
        return self.pos()