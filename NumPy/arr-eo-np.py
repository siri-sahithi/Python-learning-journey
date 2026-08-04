import numpy as np
arr=np.array([11,22,33,44,55,66])
print("Original Array:\n",arr)

#odd numbers in array 
cond=arr%2==0
newarr=arr[cond]
print("New Array with even numbers :\n",newarr)

#even numbers in array 
cond2=arr%2!=0
newarr2=arr[cond2]
print("New Array with odd numbers :\n",newarr2)
