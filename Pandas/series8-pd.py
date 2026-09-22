import pandas as pd
import numpy as np
arr = np.array([2, 3, 4, 5])
print(arr)
S1 = pd.Series(arr**2, index = range(1,5))
print('My Series is')
print(S1)
