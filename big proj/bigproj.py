#main program

#importing pandas module
import pandas as pd 

#importing numpy module
import numpy as np 

#importing matlplotlib module
import matplotlib.pyplot as plt 

#modules made specifically for program

#importing bargraph module
import bargraph as bg 

#importing appear module (for calculating how many gave the tests)
import appear as app

#importing passing module (for calculating how many passed the test)
import passing as pas 

#importing highest module (for calculating the highest in each subject)
import highest as hig

#importing subtop module(for displaying the 3 toppers of all subjects) 
import subjectop as subtop  

#importing classaverage module (for displaying the average of the whole class in any one subject)
import classaverage as cla 

#importing schoolaverage module (for calculating the school average)
import schoolaverage as scal

#importing individual module(for calculating the average score in every subject)
import individual as iv

#creating dataframe from given csv file

'''noc = input('Enter the number of columns in your file: ') #taking no. of columns 
cno = 0 
namelst = [] #list for storing names of columns

#loop for naming all the columns and storing them in the namelst

for i in range(noc):
    nameoc = input('Enter the name for column ',cno,': ')
    namelst.append(nameoc)
    cno += 1'''

namelst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

#creating the dataframe from the given csv file

df = pd.read_csv('notresan.csv',names = namelst) #names of columns derived from namelst

print(df) #displaying dataframe

#counting no. of students who appeared for exams

app.appear(df)

#f2or number of students who passed

pas.stpass(df)

#3school average

scal.scavg(df)

print(100*'-')

#5highest score in individual subject

hig.hiscore(df)

#7. for subject toppers

subtop.top(df)

#8classwise avg % in each subject

cla.clavg(df)

#individual subject average

print('Average score in each subject:')

iv.indavg(df)

print(100*'-')

#for comparing class-wise per subject

print('Class-wise comparison of marks any one subject: ')
bg.pivot(df)

print(100*'-')   
