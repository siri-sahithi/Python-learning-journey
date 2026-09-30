import pandas as pd
s1 = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
IT-Ramesh 9848353570 3
print(s1)
s2 = s1.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s2)
