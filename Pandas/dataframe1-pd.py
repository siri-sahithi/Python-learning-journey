import pandas as pd
'''
df=pd.DataFrame()
print(df)
df1=pd.DataFrame(columns=['Name','Age','rollno'])
print(df1)
'''
pro=('p-1','p-2','p-3','p-4')
cust=('cust-1','cust-2','cust-3','cust-4')
df2=pd.DataFrame(index=[cust],columns=[pro])
print(df2)
df3=pd.DataFrame(index=[cust],columns=['Name','Age','rollno'])
print(df3)
