import numpy as np
mat1=np.array([1,2,3,4,5,6,7,8,9,10])
print("Original matrix is :\n",mat1)
mat2=mat1.reshape(2,5)
print("3x2 matrix is:\n",mat2)
mat3=mat1.reshape(5,2)
print("1x3 matrix is: \n",mat3)
