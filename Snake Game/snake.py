from turtle import Turtle
from setup import Move_distance,Screen_height,Screen_width


class Snake(Turtle):
    segment_list = []

    def __init__(self):
        super().__init__()
        position_list = [(0, 0), (-20, 0), (-40, 0)]
        for position in position_list:
            new_segment = Turtle("square")
            new_segment.ht()
            new_segment.pu()
            new_segment.color("white")
            new_segment.goto(position)
            self.segment_list.append(new_segment)
        self.head = self.segment_list[0]
        # self.head.shape("arrow")
        self.head.color("blue")

    def move(self):
        self.head.showturtle()
        for x in range(len(self.segment_list)-1,0,-1):
            new_x = self.segment_list[x-1].xcor()
            new_y = self.segment_list[x-1].ycor()
            self.segment_list[x].showturtle()
            self.segment_list[x].goto(new_x,new_y)
        self.segment_list[0].fd(Move_distance)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.ht()
        new_segment.pu()
        new_segment.color("white")
        self.segment_list.append(new_segment)

    def collides(self):
        if self.head.ycor()>Screen_height//2 or self.head.ycor()< -((Screen_height-10)//2):
            return True
        elif self.head.xcor() > (Screen_width-10)//2 or self.head.xcor() < -(Screen_width//2):
            return True
        else:
            for x in range(1,len(self.segment_list)):
                if self.head.distance(self.segment_list[x]) < 10:
                    return True