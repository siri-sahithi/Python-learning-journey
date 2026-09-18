import pandas as pd
month = ["FEB", "MAR", "APR"]
days =[28, 31, 30]
S2 = pd.Series(days, month)
print(S2)
