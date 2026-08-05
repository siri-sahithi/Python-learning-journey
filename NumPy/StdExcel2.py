import numpy as np
sno,(Names,Marks) = np.genfromtxt('C:/Users/siris/OneDrive/Documents/Student_Data.csv',delimiter=',',dtype=None,skip_header=1,unpack=True)
print(Names,Marks)
