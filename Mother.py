from Ant import Ant
from Soldier import Soldier
from Police import Police
from Worker import Worker
from Larva import Larva
from random import randint

class Mother(Ant):
    def __init__(self, eat_amt, birth_qty):
        super().__init__(eat_amt)
        self.birth_quantity = birth_qty
    def give_birth(self, larvae, filepath):
        file = open(filepath, 'r')
        lines = file.readlines()
        for i in range(self.birth_quantity):
            param1 = int(lines[19].split(':')[1])
            param2 = int(lines[20].split(':')[1])
            larvae.append(Larva(param1, param2))
    def assign_work(self, soldiers, policemen, workers, larvae, filepath):
        larvae.pop()
        new_role = randint(1, 3)
        file = open(filepath, 'r')
        lines = file.readlines()
        if new_role == 1:
            param1 = int(lines[7].split(':')[1])
            param2 = int(lines[8].split(':')[1])
            soldiers.append(Soldier(param1, param2))
        elif new_role == 2:
            param1 = int(lines[11].split(':')[1])
            param2 = int(lines[12].split(':')[1])
            policemen.append(Police(param1, param2))
        else:
            param1 = int(lines[15].split(':')[1])
            param2 = int(lines[16].split(':')[1])
            workers.append(Worker(param1, param2))
