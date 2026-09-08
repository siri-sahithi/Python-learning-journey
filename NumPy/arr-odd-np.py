#create a 3X3 array only with odd numbers
import numpy as np
arr3=np.arange(1,19,2)
print("Array of odd numbers \n",arr3)
arr4=arr3.reshape(3,3)
print("3X3 odd number matrix is \n",arr4)
arr5=np.arange(2,19,2)
print("Array of even numbers \n",arr5)
arr6=arr5.reshape(3,3)
print("3X3 odd number matrix is \n",arr6)
