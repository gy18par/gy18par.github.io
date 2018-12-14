
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


'''
distance - computes distance values between agents.
pyplot - module within the matplob library allowing for basic formatting e.g.
         coordinate point colour.
'''

# In the middle ground.... humans felt compelled to build functions into 
# their code. 


# Start

import random
# import operator
import matplotlib.pyplot


# Function Declaration (defining distance)
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
            ((agents_row_a[1] - agents_row_b[1])**2))**0.5
            # not agents_row_a[0][0] - establishing distance
    

# Agent loop within function 
num_of_agents = 10
num_of_iterations = 100
agents = [] 


# Make the agents.
for i in range(num_of_agents):
    agents.append ([random.randint(0,99),random.randint(0,99)])
print (agents)


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


# Define distance 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - 
          agents[1][1])**2))**0.5
print(answer)


# Plotting distance
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0], color = 'black')
matplotlib.pyplot.show()


# Calling distance function
distance = distance_between(agents[0], agents[1])
print(distance)

# end


