class InvalidContribution(Exception):
    '''Catches if negative contribution is given.
    parameter messge -- Messge to display if negative contribution is done.
    '''
    def __init__(self,message="Contribution cann't be negative."):
        self.message = message
        super().__init__(self.message)
        


class Member:
    def __init__(self, name, contribution):
        self.name = name
        try:
            if contribution < 0:
                raise InvalidContribution

        except InvalidContribution as e:
            print(e)
            exit(1)
        
        else:
            self.contribution = contribution
        
        self.status = 0
        self.payment = 0

    def calculate(self, average):
        if self.contribution > average:
            self.payment = self.contribution - average
            self.status = 1

        elif self.contribution < average:
            self.payment = average - self.contribution
            self.status = -1
