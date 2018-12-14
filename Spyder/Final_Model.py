
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


'''
random - class generating pseudo random numbers
print - print function, often for strings
model - code which initiates, runs and tests our outputs.
agent - code which determines mathematical behaviours based on neighbourhood 
        or environment, often containing a list to allow agent communication.
environemnt - the platform or neighbourhood, a defined space in which Agents
              live. Typically a Raster grid.
Agent_Framework_classes - Agent_Framework file.
csv - comma seperated value file containing tabular data.
matplotlib - a Python 2D plotting library.
random.seed - generates a pseudorandom number which opperates on a designated
              value (agent).
import - import function of module to make it usauble within code.
operator - a symbol which performs an operation.
distance - computes distance values between agents.
pyplot - module within the matplob library allowing for basic formatting e.g.
         coordinate point colour.
requests - library used to allow user to interact language e.g. manually adding 
            strings to URL's.
bs4 - Beautiful Soup, v4 library for pulling data out of HTML and XML files.
'''


# Primary code can be found within individual practical scripts, however,
# this is my attempt to bring each weeks practical elements together in the 
# requested "Final Model" .py file. Having tested it i'm not sure it works as
# intended but I've commented each section so at the very least it should be 
# easy (ish) to follow. 


# Start

import matplotlib.pyplot
import random
import operator
import Agent_Framework_classes


# Testing console 
print ("Hello World")


# Testing console using Agent_Framework_classes
a = Agent_Framework_classes.Agent()
print (a) 


# Initialise y and x as defined value
y=50
print("y", y)
x=50
print("x", x)


# Initialise environment
environment = []
    
    
# Inititlise model parameters
num_of_agents = 10
num_of_iterations = 100
agents = []
agents.append(Agent_Framework_classes)
neighbourhood =20
random_seed = 100


# Inititlise model agents
# Make and pull agents # beware letter cases
for i in range(num_of_agents):
    random_seed += 1
    agents.append([random.randint(0,100),random.randint(0,100)])
    agents.append(Agent_Framework_classes.Agent(random_seed))
    print(agents)
    
    
# Plotting the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x) 
matplotlib.pyplot.show()


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
            
            
# Move the agents mark 2
for j in range(num_of_iterations):
    if (j % 100 == 0):
        
        
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)


# Testing agent distance calculation
def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


# Calcuclate environment eaten
total = 0
for a in agents:
    total +=()
    print(total)

# End
