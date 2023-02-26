from Ant import Ant
class Worker(Ant):
    def __init__(self, eat_amount, production_amount):
        super().__init__(eat_amount)
        self.prod_amt = production_amount
    def produce(self):
        return self.prod_amt
