import pandas as pd
import numpy as np
month = ['jan', 'feb', 'mar']
attend = (50, np.nan, 70)
Dt = dict(zip(month, attend))
print(Dt)
S1 = pd.Series(Dt)
print('My Series is')
print(S1)
