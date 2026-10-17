import pandas as pd
data = [['AJ501', "Ramesh", 45],
['AJ502', 'Suresh', 70],
['AJ503', 'kishore', 67]]
df = pd.DataFrame(data, columns=['Regd.No', 'Name', 'Marks'])
print(df)
