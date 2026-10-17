import pandas as pd
D1 ={"Mech":'I-Floor',
'CSE':'II-Floor',
'ECE':'Ground-Floor',
'Civil':'III-Floor',
}
for i, j in D1.items():
print(i, " ", j)
col = ('Dept', 'Location')
DF1=pd.DataFrame(D1, columns = col)
print(DF1)
