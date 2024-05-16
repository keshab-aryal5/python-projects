from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.score = 0
        self.goto(-280,250)
        self.file = open("high.txt","r")
        self.high_score = int(self.file.readline())
        self.file.close()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.file = open("high.txt","w")
            self.file.write(str(self.score))
            self.file.close()
        self.write(arg=f"Level: {self.score} High level: {self.high_score}",font=("Arial",20,"normal"))

    def game_over(self):
        self.home()
        self.write(arg=f"Game Over",font=("Arial",20,"normal"))

