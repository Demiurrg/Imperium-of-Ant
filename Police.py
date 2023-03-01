from Ant import Ant

class Police(Ant):
    def __init__(self, eat_amt, prod_mult):
        super().__init__(eat_amt)
        self.production_multiplier = prod_mult
        
    def stimulate(self):
        return self.production_multiplier
