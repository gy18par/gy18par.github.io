
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
'''

# In the beginning.... humans felt compelled to "aggregate individual things 
# in order to understand their mass behaviour" (Geog.leeds.ac.uk, 2018). 
# This workflow begins by allowing us to build an interactive AMB in which
# Agents are allowed to interact amoung themselves and with the environemnt.
# Here, we initialise the Agent.


# Start

import random


# testing console
print ("Hello World")


# Initialise y and x as defined value
y=50
print("y", y)
x=50
print("x", x)


# Assign x0 and y0 a pseudorandom integer between between defined values
# random_number = random.random()
# print(random_number)
x0 = random.randint(0,99)
y0 = random.randint(0,99)
print("x0", x0)
print("y0", y0)



# Randomly move y0 having set it to y
random_number = random.random()
print(random_number)
y0 = y
if random_number < 0.5 :
    y0=y0+1 #y0 += 1
else:
    y0=y0-1    
print("y0", y0)


# Randomly move x0 having set it to y
random_number = random.random()
print(random_number)
x0 = x
if random_number < 0.5 :
    x0=x0+1
else:
    x0=x0-1    
print("x0", x0)


# Assign x0 and y0 a pseudorandom integer between between defined values
x1 = random.randint(0,99)
y1 = random.randint(0,99)
print("x1", x1)
print("y1", y1)


# Randomly move y1 having set it to y
random_number = random.random()
print(random_number)
y1 = y
if random_number < 0.5 :
    y1=y1+1 #y1 += 1
else:
    y1=y1-1    
print("y1", y1)


# Randomly move x1 having set it to y
random_number = random.random()
print(random_number)
x1 = x
if random_number < 0.5 :
    x1=x1+1
else:
    x1=x1-1    
print("x1", x1)
 

# Moving forward... generate additional random numbers
random_number = random.random()
print("random_number", random_number)
if random_number < 0.5:
    x1 += 1
    print("x1 += 1")
else:
    x1 -= 1
    print("x1 -= 1")
print("x1", x1)


# Testing the distance function (5.0)
x0 = 3
x1 = 0
y0 = -4
y1 = 0


# x and x1 Agent differecne
diffx = x0 - x1
print("diffx", diffx)


# y and y1 Agent differecne
diffy = y0 - y1
print("diffy", diffy)


# Agent distance calculation
distance = (diffy**2 + diffx**2)**0.5
print("distance", distance)

def share_with_neighbours(self, neighbourhood):
    for agent in self.agents:
        dist = self.distance_between(agent) 
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))

def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


# End
   
    
'''
References

Geog.leeds.ac.uk. (2018). · Geography Programming Courses. [online] Available 
at: http://www.geog.leeds.ac.uk/courses/computing/practicals/python
/agent-framework/part1/index.html [Accessed 26 Nov. 2018].    

'''