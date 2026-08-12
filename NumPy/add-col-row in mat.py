# Add elements to the numpy matrix along with specified access. the access is not sutable flater on the
#matrix
import numpy as np
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The given matrix :\n",mat)
ncol = np.array([[11],[12],[13]])
print("New column is :\n",ncol)
mat2=np.append(mat,ncol,axis=1)
print("The matrix with new column: \n",mat2)
nrow = np.array([[11,12,13]])
mat3=np.append(mat,nrow,axis=0)
print("The matrix with new row: \n",mat3)

mat=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("The given matrix :\n",mat)
ncol = np.matrix([[11],[12],[13]])
print("New column is :\n",ncol)
mat2=np.append(mat,ncol,axis=1)
print("The matrix with new column: \n",mat2)
nrow = np.array([[11,12,13]])
mat3=np.append(mat,nrow,axis=0)
print("The matrix with new row: \n",mat3)




      
