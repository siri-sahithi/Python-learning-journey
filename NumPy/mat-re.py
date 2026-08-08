import numpy as np
mat1=np.array(range(16))
mat2=mat1.reshape(4,4)
print(mat2)
mat3=mat2[0:2,0:2]
print("the left upper sub mat:\n",mat3)
mat4=mat2[1:3,1:3]
print("the middle sub mat:\n",mat4)
mat5=mat2[2:4,2:4]
print("the right lower sub mat:\n",mat5)
mat6=np.concatenate((mat3,mat4,mat5))
print("concatenated matrix is :\n",mat6)
mat7=mat6.reshape(4,3)
print("reshaped matrix is :\n",mat7)
print("
