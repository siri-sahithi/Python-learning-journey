import numpy as np
mat1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("The given matrix :\n",mat1)
newcol = np.array([11,12,13])
print("New column is :\n",newcol)
mat2=np.insert(mat1,0,newcol,axis=1)
print("The matrix with new column at first: \n",mat2)
mat3=np.insert(mat1,3,newcol,axis=1)
print("The matrix with new column at fourth: \n",mat3)
mat4=np.insert(mat1,1,newcol,axis=0)
print("The matrix with new row at second: \n",mat4)
mat5=np.insert(mat1,2,newcol,axis=0)
print("The matrix with new row at third: \n",mat5)

