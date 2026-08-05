import numpy as np
data = np.genfromtxt('C:/Users/siris/OneDrive/Documents/Student_Data.csv',delimiter=',',usecols=[1,2],
                     dtype=None,skip_header=1)
print(data)
for row in data :
    print(row)
