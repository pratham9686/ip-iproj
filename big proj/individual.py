#module for individual subject average

#function for the same

def indavg(x):
    sub = int(input('Enter number of subjects: '))
    
    #loop for finding mean of subjects 
    
    for i in range(sub):
        nsub = input('Enter name of subject: ')
        print('Average score of the subject: ',x[nsub].mean())
        