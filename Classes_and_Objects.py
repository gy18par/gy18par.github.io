
"""
//www.python.org/psf/license/
@author: gy18par
"""
 
# -*- coding: utf-8 -*-
# __version__ 1.0.0


'''
Agent_Framework_classes - Agent_Framework file
'''

# Slightly after the middle ground.... humans felt compelled to convert their 
# object oriented code to allow agents to adopt properties and behaviour.


# Start

import random
import operator
import matplotlib.pyplot
import Agent_Framework_classes 


# CSV read in code
# file directory is important 
# multiple object list
import csv
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        for value in row:
            print(value)  


# Reading in to environment
rowlist = []	
environment = []
environment.append(rowlist)
rowlist.append(value)

 
# Defining Agents
num_of_agents = 10
num_of_iterations = 100
agents = []
agents.append(Agent_Framework_classes)

random_seed = 100


# Make and pull agents
# beware letter cases
for i in range(num_of_agents):
    random_seed += 1
    agents.append([random.randint(0,100),random.randint(0,100)])
    agents.append(Agent_Framework_classes.Agent(random_seed))
    print(agents)
   

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i]._y = (agents[i]._y + 1) % 100
        else:
            agents[i]._y = (agents[i]._y - 1) % 100

        if random.random() < 0.5:
            agents[i]._x = (agents[i]._x + 1) % 100
        else:
            agents[i]._x = (agents[i]._x - 1) % 100
            
            
# Plot agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x)
matplotlib.pyplot.show()

# end 

# agents[i].move()

