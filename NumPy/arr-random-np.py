#write a numpy program to generate a 4X3 matrix by using random numbers
import numpy as np
arr=np.random.normal(1,3,12)
print(arr)
arr=arr.reshape(4,3)
print("4X3 Matrix\n",arr)

#write a numpy program to generate array from 1 to 13 but display excluding 1 & 13
arr1=np.arange(1,14)
print("Original array is\n", arr1)
arr2=arr1[1:-1]
print("Excluding  1 and 13 is \n",arr2)


