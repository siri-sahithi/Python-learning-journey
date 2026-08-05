import numpy as np
mat=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(mat)
print(np.mean(mat))
print("mean of column in the mat:\n",np.mean(mat,axis=0))
print("mean of rows in the mat:\n",np.mean(mat,axis=1))
print("median of column in the mat:\n",np.median(mat,axis=0))
print("median of rows in the mat:\n",np.median(mat,axis=1))
