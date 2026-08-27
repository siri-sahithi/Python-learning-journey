#write a python program to calculate sum of all elements in a matrix at the same time calculate the sum
#of rows and sum of columns
import numpy as np
mat=np.arange(1,10).reshape(3,3)
print("Given matrix is :\n",mat)
print("Sum of all elements :",np.sum(mat))
print("Sum of rows elements:",np.sum(mat,axis=0))
print("Sum of columns elements:",np.sum(mat,axis=1))

