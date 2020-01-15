import matplotlib.pyplot as plt

def clavg(x):
    print('For comparing average in each subject:')

    nos = int(input('Enter no. of subjects:'))

    for i in range(nos):
        marks = input("Enter the column for marks: ")
        comp = input("Enter the column for comparison: ")
        pivdf = x.pivot_table(columns = comp, values = marks, aggfunc = 'mean')
        print(pivdf)

        pivdf.plot(kind = 'bar', title = 'Comparison of subject section-wise')

        plt.show()
    
    print('Class-wise average of chosen subject: ')

    print(100*'-')
