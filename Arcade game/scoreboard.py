from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.ht()
        self.pu()
        self.goto(position)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}",font=("Arial",60,"normal"))


