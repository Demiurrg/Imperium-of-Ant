from Ant import Ant
class Soldier(Ant):
    def __init__(self, eat_amount, kill_quantity):
        super().__init__(eat_amount)
        self.kill_qty = kill_quantity
    def kill(self, parasite_list):
        for i in range(self.kill_qty):
            if (parasite_list):
                parasite_list.pop()