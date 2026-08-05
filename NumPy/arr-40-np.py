import numpy as np
arr=np.array([11,22,33,44,55,66,77,88,99])
#first method
arr2=[]
for ele in arr:
    if ele >=40 :
        arr2.append(True)
    else :
        arr2.append(False)
print("Filter content :",arr2)
newarr=arr[arr2]
print("Elements greater than 40 is:",newarr)

#Second method
b=arr>40
c=arr[arr>40]
print("Elements greater than 40:",c)


