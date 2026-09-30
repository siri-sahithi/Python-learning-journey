import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("\nData Series after adding some data:")
s2 = pd.concat([s1, pd.Series([500, "php"])], ignore_index=True)
print(s2)
