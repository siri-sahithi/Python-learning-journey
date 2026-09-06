import numpy as np
#create a matrix using numpy matix function
mat1=np.matrix('1 2;3 4;5 6')
print(mat1)
print("Data type of the matrix", mat1.dtype)
print("No of elements ", mat1.size)
print("Dimension of matrix ", mat1.shape)
print(type(mat1))
print("\n")

#create a matrix using numpy array and also comparing the arrayfunction and matrixfunction
mat2=np.array([[1,2],[3,4]])
print(mat2)
print(type(mat2))
mat3=np.matrix(mat2)
print(mat3)
print(type(mat3))
print(mat2.shape)
print(mat3.shape)
print(mat2.dtype)
print(mat3.dtype)
print("\n")

#matrix multiplications in different ways
m1=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
#m2=np.array(reversed(m1))
print(m1)
m2=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m2)
print("Multiplication of the matrix :\n",m1*m2)
print("Original Multiplication of the matrix using @ :\n",m1@m2)
#another way to do multiplication operation
m3=np.dot(m1,m2)
print("Original Multiplication of the matrix :\n",m3)
m4=np.matmul(m1,m2)
print("Original Multiplication of the matrix :\n",m4)
