import pandas as pd
L = [2, 3, 4, 5, None]
print(L)
S = pd.Series(L * 2)
print('My Series is')
print(S)
