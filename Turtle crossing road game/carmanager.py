from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.carlist = []
        self.color = ["red","green","blue","yellow","orange","pink","black","purple","violet","maroon","sky blue"]
        self.move_distance = 5

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.pu()
            new_car.color(random.choice(self.color))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.goto(300,random.randint(-250,250))
            self.carlist.append(new_car)

    def move_car(self):
        for car in self.carlist:
            car.bk(self.move_distance)
