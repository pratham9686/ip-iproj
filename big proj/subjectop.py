def top(x):
    print('For finding the toppers of each subject:' )
    sno = 1
    nos = int(input('Enter number of subjects: '))
    sublst = []
    ui = input('Enter name of column used for unique identification of each row: ')

    for i in range(nos):
        cols = input('Enter name of column containing subject marks: ')
        sublst.append(cols)
        adf = x[[ui ,cols]]
        sadf = adf.sort_values(cols)
        print('Toppers of this subject are: ')
        print(sadf.tail(3))
        sno+=1
  
    print(100*'-')
