
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


'''
matplotlib - a Python 2D plotting library.
random.seed - generates a pseudorandom number which opperates on a designated
              value (agent).

'''


# Shortly after the beginning.... humans felt compelled to store their agents 
# in containers.


# Start

import matplotlib.pyplot 
import random
import operator 


# Setting random_number between 0 and 1
random_number = random.random()
print(random_number)


# Allowcating agents a random_number between 0 and 100
y0 = random.randint(0,99)
x0 = random.randint(0,99)


'''
Simplified version (seed)
random_seed = 0
random.seed(random_seed)
'''


# Creating Agent lists for coordinates
agents = []
agents.append([y0,x0])
y0 = random.randint(0,99)
x0 = random.randint(0,99)
agents.append([y0,x0])


# Testing 
print (agents)
# agents[0][0] = 57


# Printing x or y cooridinate based on list selection
# Agents [0][0] = y, [0][1] = x
# Value determines which list cooridinate is printed
print(agents)
print(agents[0])
print(agents[0][0])
print(agents[0][1])
#print(agents[0][2])
print(agents[1])
print(agents[1][0])
print(agents[1][1])


# Distance between agents  agents
distance = ((agents[0][1] - agents[1][1])**2 + (agents[0][0] - agents[1][0])
**2)**0.5
print(distance)


# Removing x0 and y0
agents =[x0,y0]
agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)


# Plot corridinates as a graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
# matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(x0, y0, color='red')
matplotlib.pyplot.show()

# End
