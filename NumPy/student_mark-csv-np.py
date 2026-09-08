import numpy as np
path = r"C:\Users\siris\OneDrive\Documents\datasets for programs\student_marks2.csv"
data =np.genfromtxt(path,delimiter=',',names=True,dtype=None,encoding='utf-8')
for i in data:
    print(i)
