import pandas as pd
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("s1:")
print(s1)
print("s2:")
print(s2)
print("\nItems of sr1 not present in sr2:")
s3 = s1[~s1.isin(s2)]
print(s3)
