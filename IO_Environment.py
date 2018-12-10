# multiple object list

# CSV read in code
# file directory is important 
import csv
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        for value in row:
            print(value) 


# Reading in to environment - see town planning model  
rowlist = []	
environment = []
environment.append(rowlist)
rowlist.append(value)

'''
# testing
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 
'''