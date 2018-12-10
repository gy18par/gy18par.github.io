
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0 


'''
csv - comma seperated value file containing tabular data.
'''

# With the penultimate workflow in hand.... humans felt compelled enhance their
# model using animation.


# Start

import matplotlib.pyplot
import random
import Agent_Framework_classes


import csv
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        for value in row:
            print(value) 
 

# Importing html x and y data columns 
# Initializing in model

import requests 
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


# Initialising Agents
num_of_agents = 1  # Actually creates the environments e.g. Figure 1
num_of_iterations = 100
agents = []

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

# Animation
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
    # code line error

carry_on = False
    
    
# Updating environment
def update(frame_number): 
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(), color="black")
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


        if False:
            if (carry_on):
                for i in range(num_of_agents):
                    agents[i].move()
                    agents[i].eat()
                    agents[i].share_with_neighbours()
                    print (False)
               
                
# Plot environment
matplotlib.pyplot._x (0,99(environment))
matplotlib.pyplot._y (0,99(environment[0]))
matplotlib.pyplot.show (environment)

for i in range(num_of_agents):
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()

# End


