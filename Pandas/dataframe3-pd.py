import pandas as pd
import numpy as np
Sno=[532,553,572]
Name=["Keerthi","SriLakshmi","SiriSahithi"]
#we used nan for just example of missing data like that 
Age=[19,19,np.nan]
data=zip(Sno,Name,Age)
df=pd.DataFrame(data,)
print(df)
print("\n")
meow=["Roll.No","Name","Dept","Section"]
row=['1','2','3','4']
roll=[532,553,569,572]
name=["Keerthi","pichi","mouni","siri"]
Dept=["CSE","CSE","CSE","CSE"]
sec=['A','A','A','A']
data=zip(roll,name,Dept,sec)
print(pd.DataFrame(data,columns= meow,index=row))
