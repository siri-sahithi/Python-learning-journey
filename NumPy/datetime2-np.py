import numpy as np
dt=np.datetime64("now")
print("Today's date and time:",dt)
date=np.datetime64("today","D")
print("complete date is:",date)
month=np.datetime64("today","M")
print("month and year is:",month)
year=np.datetime64("today","Y")
print("Current year is:",year)
hours=np.datetime64("now","h")
print("current hours is :",hours)
mins=np.datetime64("now","m")
print("current minutes is:",mins)
sec=np.datetime64("now","s")
print("current seconds is:",sec)


#Question-3
import numpy as np
x="2026-08-12T09:30:21"
print("Given string is:",x,"\n type is",type(x))
year=np.datetime64("2026-08-12T09:30:21","Y")
mont=np.datetime64("2026-08-12T09:30:21","M")
date=np.datetime64("2026-08-12T09:30:21","D")
hour=np.datetime64("2026-08-12T09:30:21","h")
mins=np.datetime64("2026-08-12T09:30:21","m")
sec=np.datetime64("2026-08-12T09:30:21","s")
print(year)
print(mont)
print(date)
print(hour)
print(mins)
print(sec)

#Question-4
import numpy as np
from datetime import datetime
dt64=np.datetime64("2026-08-12T09:30:21")
print("numpy date",dt64)
dt=dt64.astype(datetime)
print("python date",dt)





