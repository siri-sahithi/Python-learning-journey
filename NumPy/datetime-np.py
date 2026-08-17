#write a numpy a program python date to numpy date
import numpy as np
from datetime import datetime
pdt = datetime(2026,8,13,14,29,14)
print(pdt)
print(type(pdt))
ndt =np.datetime64(pdt)
print(ndt)

#display the all the dates between two dates in numpy
#dates =np.arange('2026-August-13','2026-September-01', dtype='datetime64[D]')
#print("Range of Dates :\n",dates)
dates =np.arange('2026-08-13','2026-09-01', dtype='datetime64[D]')
print("Range of Dates horizontal :\n",dates)
print("Dates vertically\n",dates[:,None])
