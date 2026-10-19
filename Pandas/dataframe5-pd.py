import pandas as pd
T1= (1, 2, 3, 4, 5)
T2= ('civil', 'EEE', 'Mech', 'ECE', 'CSE')
T3= ('Koti', 'Veeraih', 'Praneeth', 'Ramesh', 'Chiru')
Data = zip(T1, T2, T3)
col = ['Dept.No', 'Name', 'HOD']
df = pd.DataFrame(Data, columns=col)
print(df)
