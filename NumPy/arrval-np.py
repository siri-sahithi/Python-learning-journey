import numpy as np
arr=np.array([1,2,3,4,5])
val=int(input("enter value:"))
if val in arr:
    print(val,"available")
else:
    print(val,"not available")
    
index=np.where(val==arr)
print(index)
        
