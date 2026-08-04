import numpy as np
a= np.array([1,2,3,4,5])
print(a.dtype)
print("First element address ", id(a[0]))
for i in a-1 :
    print(id(a[i]))
