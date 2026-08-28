import numpy as np
arr=np.array([1,2,3,4])
print("Given array is:\n",arr)
x=arr.size
y=arr.itemsize
print("Number of elements in array:",x)
print("Memory occupency of one element in array:",y)
print("Total amount of memory occupied by the array is:",x*y)


import numpy as np
arr1=np.array([1,2,3,4],dtype=np.int8)
print("size of element in int8 is",arr1.itemsize)
arr2=np.array([1,2,3,4],dtype=np.int16)
print("size of element in int16 is",arr2.itemsize)
arr3=np.array([1,2,3,4],dtype=np.int32)
print("size of element in int32 is",arr3.itemsize)
arr4=np.array([1,2,3,4],dtype=np.int64)
print("size of element in int64 is",arr4.itemsize)
arr5=np.array([1,2,3,4],dtype=np.float16)
print("size of element in float16 is",arr5.itemsize)
arr6=np.array([1,2,3,4],dtype=np.complex128)
print("size of element in complex128 is",arr6.itemsize)


import numpy as np
arr1=np.array([1,2,3,4],dtype=np.int8)
print(arr1)
print("element size of array-1",arr1.itemsize)
arr2=arr1.astype(np.float16)
print(arr2)
arr1=arr1.astype(np.complex128)
print(arr1)
