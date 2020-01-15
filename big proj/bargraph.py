import pandas as pd
import matplotlib.pyplot as plt

def pivot(x):
    
    marks = input("Enter the column for marks: ")
    comp = input("Enter the column for comparison: ")

    pivdf = x.pivot_table(columns = comp, values = marks, aggfunc = 'mean')

    print(pivdf)

    pivdf.plot(kind = 'bar', title = 'Class-wise comparison per subject')

    plt.show()

    
    
