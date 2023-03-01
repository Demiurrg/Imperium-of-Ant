from Ant import Ant

class Larva(Ant):
    def __init__(self, eat_amt, growth_time):
        super().__init__(eat_amt)
        self.grow_time = growth_time