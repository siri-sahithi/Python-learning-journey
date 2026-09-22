import pandas as pd
keys = ["apple", "banana", "cherry"]
default_value = 0
fruit_counts = dict.fromkeys(keys, default_value)
print(fruit_counts)
print(type(fruit_counts))
S1 = pd.Series(fruit_counts)
print(S1)
