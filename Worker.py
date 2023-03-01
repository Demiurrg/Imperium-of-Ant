from Ant import Ant

class Worker(Ant):
    def __init__(self, eat_amt, prod_amt):
        super().__init__(eat_amt)
        self.production_amount = prod_amt
    def produce(self):
        return self.production_amount
