from Ant import Ant
from Mother import Mother
from Soldier import Soldier
from Police import Police
from Worker import Worker
from Larva import Larva
from Parasite import Parasite
import os
import time
import math
class Anthill:
    def __init__(self, filepath):
        self.filepath = filepath
        file = open(filepath, 'r')
        lines = file.readlines() # all file lines
        self.supplies = int(lines[1].split(':')[1]) # second line from the file, split by : symbol
        # we take second part of it to get the number of supplies at the begging
        self.mother = Mother(int(lines[3].split(':')[1]), int(lines[4].split(':')[1])) 
        # same shit, we get parameters for mother
        self.soldiers = []
        self.policemen = []
        self.workers = []
        self.larvae = []
        self.parasites = []
        for ant_list, ant_type, i in zip((self.soldiers, self.policemen, self.workers, self.larvae), (Soldier, Police, Worker, Larva), range(0, 19, 4)): 
            # as some classes have the same amount of parameters, we can read them from the file with a cycle 
            list_len = int(lines[6+i].split(':')[1])
            param1 = int(lines[7+i].split(':')[1])
            param2 = int(lines[8+i].split(':')[1])
            for j in range(list_len):
                ant_list.append(ant_type(param1, param2))
        list_len = int(lines[22].split(':')[1]) # parasites have only one parameter, they go separately
        param1 = int(lines[23].split(':')[1])
        for j in range(list_len):
            self.parasites.append(Parasite(param1))
    def day(self): # anthill one day simulation
        self.supplies -= self.mother.eat() # mother eats
        if self.supplies < 0:
            self.supplies = 0
            self.mother = None
            return 0 # mother is dead, game over
        for ant_list in (self.soldiers, self.policemen, self.parasites, self.larvae, self.workers): # ants eat
            if (ant_list):
                for ant in ant_list:
                    self.supplies -= ant.eat()
                    if self.supplies < 0: # there is not enough food
                        self.supplies = 0 # the barn is empty, my lord
                        ant_list.pop() # every hungry ant dies
        self.mother.give_birth(self.larvae, self.filepath) # larvae are born 
        for ant in self.larvae: # larvae are growing
            if ant.grow_time == 0: # if they did their time
                self.mother.assign_work(self.soldiers, self.policemen, self.workers, self.larvae, self.filepath) # they grow into someone
            else:
                ant.grow_time -= 1 # else wait
        for ant in self.soldiers: 
            ant.kill(self.parasites) # soliders kill parasites
        today_prod = 0
        for ant in self.workers: 
            today_prod += ant.produce() # Work, niggers, the sun is still high!
        for ant in self.policemen:
            today_prod *= (1 + ant.stimulate()/100) # policemenmen multiply supplies
        self.supplies += math.floor(today_prod) # today's production is added to the pile
        return 1 # everything is fine so far
    def indication(self): # print function for us to see anthill's numbers
        print('The amount of food :', self.supplies)
        for ant, quantity in zip(('Soldiers', 'Police', 'Workers', 'Larvae', 'Parasites'), (self.soldiers, self.policemen, self.workers, self.larvae, self.parasites)):
            print(ant, ':', len(quantity))
        print('\n')
    def life(self):
        os.system('cls')
        self.indication()
        while(self.day()):
            self.indication()
            time.sleep(1)
        print('Well, shit, mother died. Game over.\n')
            
        
