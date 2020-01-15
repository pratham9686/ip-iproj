import pandas as pd
import numpy as np

namelst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

#creating the dataframe from the given csv file

df = pd.read_csv('notresan.csv',names = namelst) #names of columns derived from namelst

print(df) #displaying dataframe

namelst = []

nos = input("Enter column for names of students: ")

noc = int(input("Enter the no. of columns that contain marks: "))

st = 0
ct = 1
nsum = 0
a = 0

for i in range(noc):
    nameoc = input("Enter the name of the column: ")
    namelst.append(nameoc)

for i in namelst:    
    print(df.groupby(i)[namelst].transform(np.mean))

'''for i in range(384): 
    adf = df.iloc[st:ct,:]
    for x in namelst:    
        print(adf[x])
    print(asum)    
    st += 1
    ct += 1    '''
    
'''for i in df.iterrows():
    print(i)

for i in namelst:
    print(df[i].sum()/384)
    
print(namelst)    '''