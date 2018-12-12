
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


# Agent_Framework_classes workflows 


# Start 

import random

x: int = random 
y: int = random 

 
# agents (int)
# agents = Agent_Framework_classes.agent() 


# Defining Agent
class Agent():
    
    def __init__(self, random_seed):
        random.seed(random_seed)
        self._x = random.randint(0,99)
        self._y = random.randint(0,99) 

       
# Finding agent
def __init__ (self, _x, _y):
        pass
        self.x = _x
        self.y = _y
def x(self):
       return self._x, self._y   
       
  
# Moving in enviroment 
def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100    
 
       
# Interacting with environment         
def eat(self):
        
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
        
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
          
          
# Agent interaction within environment (neighbourhood)
          def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average
                #print("distance = " + str(distance))
        
# End

