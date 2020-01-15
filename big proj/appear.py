# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:25:18 2020

@author: Senior Lab
"""

def appear(x):
    print(100*'-')
    total = 0
    print('Number of students who appeared for the exam: ')
    for i in x.iterrows(): #loop for counting no. of students who passed
        total = total + 1
    print(total) #displaying result

    print(100*'-')