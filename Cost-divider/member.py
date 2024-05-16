class Member:
    def __init__(self,name,contribution):
        self.name = name
        self.contribution = contribution
        self.status = 0
        self.payment = 0

    def calculate(self,average):
        if self.contribution > average:
            self.payment = self.contribution - average
            self.status = 1

        elif self.contribution < average:
            self.payment = average - self.contribution
            self.status = -1