
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0 


'''
csv - comma seperated value file containing tabular data.
requests - library used to allow user to interact language e.g. manually adding 
            strings to URL's.
bs4 - Beautiful Soup, v4 library for pulling data out of HTML and XML files.
'''

# The end is nigh.... and humans felt compelled to run thier models from a
# GUI, incorporating a run menu.


# Start

import matplotlib.backends.backend_tkagg
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import requests
import bs4


# Parameters
num_of_agents = 20
num_of_iterations = 20
neighbourhood = 1
random_seed = 100
agent_store = 100
    
    
# Initialise GUI main window
root = tkinter.Tk()
root.wm_title("Model")


# Getting html data from web (column information)
url = 'https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
td_zs = soup.find_all(attrs={"class" : "z"})


# Initialise the agent environment 
environment = []


# Dsiplay plot in model window
def run(Matplotlib_Animation):
	model_menu.entryconfig("Run model", state="disable")
Matplotlib_Animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
canvas.draw()


# Animation 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Improving GUI window
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="The model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
w = tkinter.Canvas(root, width=200, height=200)
w.pack()
w.create_rectangle(0, 0, 200, 200, fill="blue")
tkinter.mainloop()

# End


