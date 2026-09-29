import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
IT-Ramesh 9848353570 2
print(s1)
s2 = pd.Series(s1).sort_values()
print(s2)
