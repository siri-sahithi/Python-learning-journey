#write a numpy program to find sum of diagonal elements of an array '
import numpy as np
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The given matrix :\n",mat)
ds=np.trace(mat)
print("the sum of the diagonal elements is: ",ds)
