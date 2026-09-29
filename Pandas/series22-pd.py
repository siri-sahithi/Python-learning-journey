import pandas as pd
s1 = pd.Series([
['Red', 'Green', 'White'],
['Red', 'Black'],
['Yellow']])
print("Original Series of list")
print(s1)
s2 = s1.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s2)
