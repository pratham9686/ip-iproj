# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:41:34 2020

@author: Senior Lab
"""
def hiscore(x):
    print('For finding the highest score in each subject:')

    sno = 1
    nos = int(input('Enter number of subjects: '))
    sublst = []

    for i in range(nos):
        cols = input('Enter name of column containing subject marks: ')
        sublst.append(cols)
  
    for i in sublst:
        print('')
        print('Highest in subject no.',sno)
        print(x[i].max())
        sno+=1
    
    print(100*'-')  

