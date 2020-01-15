#module for computing school average

#function for computing school average

def scavg(x):
    sub = int(input('Enter number of subjects: '))
    
    subsum = 0
    
    #loop for finding mean of subjects 
    
    for i in range(sub):
        nsub = input('Enter name of subject: ')
        submn = x[nsub].mean()
        subsum += submn
        
    print('The school average is: ',subsum/sub)    