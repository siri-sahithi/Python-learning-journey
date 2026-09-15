import numpy as np
mat1=np.matrix([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])
print("The given matrix :\n",mat1)
con= mat1>5
print(mat1[con])
