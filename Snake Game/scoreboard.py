from turtle import Turtle
from setup import Pen_width,Screen_width,Screen_height


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.ht()
        self.pu()
        self.width(Pen_width)
        self.score = -1
        self.file = open("high.txt","r")
        self.high_score = int(self.file.readline())
        self.file.close()


    def update_score(self):
        self.clear()
        self.score += 1
        if self.high_score < self.score:
            self.file = open("high.txt","w")
            self.file.write(str(self.score))
            self.file.close()
        file = open("high.txt","r")
        score = int(file.readline())
        file.close()
        self.goto(0,(Screen_height//2)-50)
        self.write(arg=f"Score: {self.score} High score: {score}",align="center",font=("arial",15,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.file = open("high.txt","r")
        self.high_score = self.file.readline()
        self.file.close()
        self.write(arg=f"Game Over !!!\nScore: {self.score}\nHigh score:{self.high_score}",align="center",font=("arial",15,"normal"))