from Ant import Ant

class Soldier(Ant):
    def __init__(self, eat_amt, kill_qty):
        super().__init__(eat_amt)
        self.kill_quantity = kill_qty
    def kill(self, parasites):
        for i in range(self.kill_quantity):
            if (parasites):
                parasites.pop()