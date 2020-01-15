# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:32:44 2020

@author: Senior Lab
"""

import pandas as pd

def stpass(x):
    stpass = 0

    crit = input('Enter column for determining pass or fail: ')

    pfdf = pd.DataFrame(x[crit])

    for k,i in pfdf.iterrows():
        if i[crit] == 'PASS':
            stpass += 1        
    print('Number of students who passed: ',stpass)

    print(100*'-')