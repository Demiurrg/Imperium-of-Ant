# during the Great Patriotic War in the temporarily occupied areas,
# Polizei - a local resident serving in the Nazi police

from Ant import Ant
class Polizei(Ant):
    def __init__(self, eat_amount, production_modif):
        super().__init__(eat_amount)
        self.prod_mod = production_modif
    def stimulate(self):
        return self.prod_mod
