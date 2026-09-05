#create a 5X5 matrix where boarders are 1's and remaining all elements are 0's
mat=np.ones((5,5))
print("Matrix of all ones\n",mat)
mat[1:-1,1:-1] = 0
print("Matrix with boarders:\n",mat)
