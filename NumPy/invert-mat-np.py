#create an array with 0-20 numbers & then print the first 8 with +ve sign and remaining -ve sign
import numpy as np
arr7=np.arange(21)
print("Original matrix \n",arr7)
arr7[(arr7>=9)&(arr7<=15)]*=-1
print("The Invert matrix \n",arr7)

#create an array with 0-20 elements then invert the sign of elements from 9 to 15 as a new array
arr7=np.arange(21)

arr8=arr7[(arr7>=9)&(arr7<=15)]*-1
print("the invert matrix \n",arr8)

