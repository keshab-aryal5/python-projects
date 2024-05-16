from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        self.move_distance = 8

    def move_player(self):
        self.fd(self.move_distance)

    def reset(self):
        self.goto(0,-280)

    def increase_speed(self):
        self.move_distance += 1
