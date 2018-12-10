# IO model - creating environment 

# import data for agent environment and get them to interact

import random
#import operator
import matplotlib.pyplot
import Agent_Framework_classes 

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
            ((agents_row_a.y - agents_row_b.y)**2))**0.5  


# Defining Agents
num_of_agents = 10
num_of_iterations = 100
agents = []

#agentframework.Agent()
#print (agent())

random_seed = 200


# Make and pull agents
for i in range(num_of_agents):
    random_seed += 1
    agents.append([random.randint(0,100),random.randint(0,100)])
    agents.append(Agent_Framework_classes.Agent(random_seed))
    print(agents)
    
# Testing random
#print(a.y, a.x)
#a.move()
#print(a.y, a.x)


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
         
        if random.random() < 0.5:
            agents[i]._y = (agents[i]._y + 1) % 100
            # y has no attribute
else:
            agents[i]._y = (agents[i]._y - 1) % 100

if random.random() < 0.5:
            agents[i]._x = (agents[i]._x + 1) % 100
else:
            agents[i]._x = (agents[i]._x - 1) % 100

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# end 
