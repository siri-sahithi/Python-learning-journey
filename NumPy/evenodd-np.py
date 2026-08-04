import numpy as np
arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("The Given array is\n",arr)
earr=np.array([])
oarr=np.array([])
for i in arr-1:
    if(arr[i]%2!=0):
        oarr=np.append(oarr,arr[i])
    else :
        earr=np.append(earr,arr[i])
print("Array with odd numbers s:\n",oarr)
print("Array with even numbers s:\n",earr)

