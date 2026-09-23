import pandas as pd
S = pd.Series([12, 13, 14, 15, 16], index = ['A', 'B', 'C', 'D', 'E'])
print("Series is: ", S)
print("First and Final values is series is:")
print(S['A'], S['E'])
print("We can do the same in anotehr way:")
print(S[['A', 'E']]) 
