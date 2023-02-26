from Ant import Ant
from Soldier import Soldier
from Polizei import Polizei
from Worker import Worker
from Larva import Larva
from random import randint
class Mother(Ant):
    def __init__(self, eat_amount, birth_quantity):
        super().__init__(eat_amount)
        self.birth_qty = birth_quantity
    def give_birth(self, larva_list, filepath):
        file = open(filepath, 'r')
        lines = file.readlines()
        for i in range(self.birth_qty):
            param1 = int(lines[19].split(':')[1])
            param2 = int(lines[20].split(':')[1])
            larva_list.append(Larva(param1, param2))
    def assign_work(self, soldier_list, polizei_list, worker_list, larva_list, filepath):
        larva_list.pop()
        new_role = randint(1, 3)
        file = open(filepath, 'r')
        lines = file.readlines()
        if new_role == 1:
            param1 = int(lines[7].split(':')[1])
            param2 = int(lines[8].split(':')[1])
            soldier_list.append(Soldier(param1, param2))
        elif new_role == 2:
            param1 = int(lines[11].split(':')[1])
            param2 = int(lines[12].split(':')[1])
            polizei_list.append(Polizei(param1, param2))
        else:
            param1 = int(lines[15].split(':')[1])
            param2 = int(lines[16].split(':')[1])
            worker_list.append(Worker(param1, param2))
