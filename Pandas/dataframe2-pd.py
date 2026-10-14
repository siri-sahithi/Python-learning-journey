import pandas as pd
Roll = (501, 502, 503, 504, 505)
Name = ['Ramesh', 'Suresh', 'Sateesh', 'Jagadesh', 'Kumar']
Age= (45, 34, 27, 39, 52)
Data =zip(Roll, Name, Age)
DF1 = pd.DataFrame(Data, columns=['S.No', 'Name', 'Age'])
print(DF1)
#Set column index for one of the column in DataFrame
print('\n')
DF2 =DF1.set_index('S.No')
print(DF2)
print('\n')
L1 = ['Ramesh', 'Suresh', 'Venkatesh', 'Rajesh', 'kalpana', 'Vimala']
DF1=pd.DataFrame(Data,DF2)
print(DF1)
