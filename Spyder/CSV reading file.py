# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:19:05 2018

@author: gy18par
"""

import csv
with open('in.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        for value in row: 
            print(value) 
