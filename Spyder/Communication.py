
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


''' 
csv - comma seperated value file containing tabular data.
'''

# With the end looming.... humans felt compelled to alter their agents
# variables to allow them to communicate with one another.


# Start

import Agent_Framework_classes
# import random
# import operator
import matplotlib.pyplot


# Listing agents in a neighbourhood
# share_with_neighbours(neighbourhood)


# CSV read in code
# file directory is important 
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
agents.append(Agent_Framework_classes.Agent(environment))

neighbourhood =20
random_seed = 100


# Make and pull agents
for i in range(num_of_agents):
    random_seed += 1
    #agents.append([random.randint(0,100),random.randint(0,100)])
    agents.append(Agent_Framework_classes.agents (random_seed))
    print(agents)
    
     
# Initialise environment
    environment = []


# Move the agents.
for j in range(num_of_iterations):
    if (j % 100 == 0):
        
        
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
        
# Agent method decloration
print (neighbourhood)

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) + 
            ((agents_row_a._y - agents_row_b._y)**2))**0.5


# Plot Agents on environment
matplotlib.pyplot.xlim(0, 99)(environment)
matplotlib.pyplot.ylim(0, 99)(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y) 
matplotlib.pyplot.show()


# Calcuclate environment eaten
total = 0
for a in agents:
    total +=()
    print(total)

# End


