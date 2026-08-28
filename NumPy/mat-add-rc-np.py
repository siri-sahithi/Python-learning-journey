#write a Numpy program to add new row to the existing matrix
import numpy as np
mat=np.arange(1,10).reshape(3,3)
print("Give matrix is :\n",mat)
new_row=np.array([[6,6,6]])
mat1=np.append(mat,new_row,axis=0)
print("After adding a row using append:\n",mat1)
#write a numpy program to insert a new row at required position
mat2=np.insert(mat,0,new_row,axis=0)
print("inserting row at first :\n",mat2)
mat3=np.insert(mat,1,new_row,axis=0)
print("inserting row at second :\n",mat3)
mat4=np.insert(mat,2,new_row,axis=0)
print("inserting row at third :\n",mat4)
mat5=np.insert(mat,3,new_row,axis=0)
print("inserting row at last :\n",mat5)

#write a numpy program to add new column to the existing matrix
new_col=np.array([[6],[6],[6]])
mat6=np.append(mat,new_col,axis=1)
print("After adding a column using append:\n",mat6)
#write a numpy program to insert a new column at required position
mat7=np.insert(mat,0,new_row,axis=1)
print("inserting column at first :\n",mat7)
mat8=np.insert(mat,1,new_row,axis=1)
print("inserting column at second :\n",mat8)
mat9=np.insert(mat,2,new_row,axis=1)
print("inserting column at third :\n",mat9)
mat10=np.insert(mat,3,new_row,axis=1)
print("inserting column at last :\n",mat10)

#Write a numpy program to add same value thrice as a column
