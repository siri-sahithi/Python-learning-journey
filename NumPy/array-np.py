#1
import numpy as np
a=np.array([501,502,503,504,505,506,507])
m=np.array([45,None,56,74,None,47,None])
for i in range(len(m)):
    if(m[i]is None):
        print(a[i])
#2
import numpy as np
student =np.array(['A','B','C','D','E','F','G'])
marks=np.array([45,84,56,74,26,47,55])
for i in range(len(marks)):
    if(marks[i]<50):
        print(student[i])
#3
import numpy as np
girls=np.array(["Ravali","Rani","Revathi","Ramya"])
boys=np.array(["Raju","Ramu","Ranga"])
c=np.concatenate([girls,boys])
print(c)


#5
a=np.array([21,23,17,19,14,13,10,7,9,14])
c=np.array([])
for i in a-1:
    m=a[i]+6
    c=add(m)
print(c)
