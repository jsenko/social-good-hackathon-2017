class paramGenerator:
    def __init__(self, fromYear, toYear, druhyVeci = ['a','b']): #including start and end year
        self.druhyVeci = druhyVeci
        self.druhyVeci_iterator = iter(druhyVeci)
        self.params = [
            fromYear, 
            1, 
            next(self.druhyVeci_iterator), 
            1
        ] 
        self.successiverFails = 0

    def next(self):
        self.successiverFails = 0
        self.params[3] += 1
        return self.params

    def fail(self):
        if self.params[3] == 1:
           self.successiverFails += 1
        if self.successiverFails == len(self.druhyVeci):
           self.druhyVeci_iterator = iter(self.druhyVeci)
           self.params[0] += 1
           self.params[1] = 1
           self.params[2] = next(self.druhyVeci_iterator) 
           self.params[3] = 1
           return self.params
        try:
           self.params[2] = next(self.druhyVeci_iterator)
           self.params[3] = 1
           return self.params
        except StopIteration:
           self.druhyVeci_iterator = iter(self.druhyVeci)
           self.params[1] += 1
           self.params[2] = next(self.druhyVeci_iterator)
           self.params[3] = 1
           return self.params


