
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


'''
import - import function of module to make it usauble within code
operator - a symbol which performs an operation
'''


# Not far from the beginning.... humans felt compelled to rework their code
# using control flow statements so that it appeared "cleaner".


# Start

# import operator
import matplotlib.pyplot 
import random


# Adding agent variable (setting environment)
# Interchangable by user
num_of_agents = 5


# Defining number of movements and initialising agent
num_of_iterations = 100 
agents = []


# Setting coordinates and creating agents via looping 
# Important to indent line inside loop
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)


# For every agent
for i in range(num_of_agents):
    # move agent
    if random.random() < 0.5:
        agents[i][0] += 1
    else:
        agents[i][0] -= 1

    if random.random() < 0.5:
        agents[i][1] += 1
    else:
        agents[i][1] -= 1
        

# Testing (legal move)    
print(agents)


# Moving looped coordinates twice
if random.random() < 0.5:
    agents[0][0] += 2
else:
    agents[0][0] -= 2

if random.random() < 0.5:
    agents[0][1] += 2
else:
    agents[0][1] -= 2

if random.random() < 0.5:
    agents[0][0] += 2
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 2
else:
    agents[0][1] -= 2
print (agents)


# Iterating number of agent movements 
# Setting 'y' location
for i in range(num_of_agents):
    if agents[i][0] < 0:
        agents[i][0] = 0
    if agents[i][1] < 0:
        agents[i][0] = 0
    if agents[i][0] > 99:
        agents[i][0] = 99
    if agents[i][1] > 99:
        agents[i][0] = 99


# Running multiple coordinates (agents)
matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color = 'black')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color = 'blue')
matplotlib.pyplot.show()


# Torus - Boundary solution elements in model design
# Test code against each agent  
if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100    


# End

