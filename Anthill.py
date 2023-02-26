from Ant import Ant
from Mother import Mother
from Soldier import Soldier
from Polizei import Polizei
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
        self.stock = int(lines[1].split(':')[1]) # second line from the file, split by : symbol
        # we take second part of it to get the number of supplies at the begging
        self.mother = Mother(int(lines[3].split(':')[1]), int(lines[4].split(':')[1])) 
        # same shit, we get parameters for mother
        self.army = [] # list of soldiers
        self.law = [] # list of polizei
        self.factory = [] # list of workers
        self.kindergarten = [] # list of larvae
        self.unemployed = [] # list of parasites
        for ant_list, ant_type, i in zip((self.army, self.law, self.factory, self.kindergarten), (Soldier, Polizei, Worker, Larva), range(0, 19, 4)): 
            # as some classes have the same amount of parameters, we can read them from the file with a cycle 
            list_len = int(lines[6+i].split(':')[1])
            param1 = int(lines[7+i].split(':')[1])
            param2 = int(lines[8+i].split(':')[1])
            for j in range(list_len):
                ant_list.append(ant_type(param1, param2))
        list_len = int(lines[22].split(':')[1]) # parasites have only one parameter, they go separately
        param1 = int(lines[23].split(':')[1])
        for j in range(list_len):
            self.unemployed.append(Parasite(param1))
    def day(self): # anthill one day simulation
        self.stock -= self.mother.eats() # mother eats
        if self.stock < 0:
            self.stock = 0
            self.mother = None
            return 0 # mother is dead, game over
        for ant_list in (self.army, self.law, self.unemployed, self.kindergarten, self.factory): # ants eat
            if (ant_list):
                for ant in ant_list:
                    self.stock -= ant.eats()
                    if self.stock < 0: # there is not enough food
                        self.stock = 0 # the barn is empty, my lord
                        ant_list.pop() # every hungry ant dies
        self.mother.give_birth(self.kindergarten, self.filepath) # larvae are born 
        for ant in self.kindergarten: # larvae are growing
            if ant.grow_time == 0: # if they did their time
                self.mother.assign_work(self.army, self.law, self.factory, self.kindergarten, self.filepath) # they grow into someone
            else:
                ant.grow_time -= 1 # else wait
        for ant in self.army: 
            ant.kill(self.unemployed) # soliders kill parasites
        today_prod = 0
        for ant in self.factory: 
            today_prod += ant.produce() # Work, niggers, the sun is still high!
        for ant in self.law:
            today_prod *= (1 + ant.stimulate()/100) # Lawmen multiply supplies
        self.stock += math.floor(today_prod) # today's production is added to the pile
        return 1 # everything is fine so far
    def indication(self): # print function for us to see anthill's numbers
        print('The amount of food :', self.stock)
        for ant, qty in zip(('Soldiers', 'Polizei', 'Workers', 'Larvae', 'Parasites'), (self.army, self.law, self.factory, self.kindergarten, self.unemployed)):
            print(ant, ':', len(qty))
        print('\n')
    def life(self):
        os.system('cls')
        self.indication()
        while(self.day()):
            self.indication()
            time.sleep(1)
        print('Well, shit, mother died. Game over.\n')
            
        
