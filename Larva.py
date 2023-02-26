from Ant import Ant
class Larva(Ant):
    def __init__(self, eat_amount, growth_time):
        super().__init__(eat_amount)
        self.grow_time = growth_time
