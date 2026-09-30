import pandas as pd
s1 = pd.Series([10,11,12,13,14,15,16,17,18,19,20])
print("Original Data Series:")
print(s1)
print("\nSubset of the above Data Series:")
n = 16
s2 = s1[s1 < n]
print(s2)
