#TimeDelta
import numpy as np
day=np.timedelta64(3,'D')
month = np.timedelta64(8,'M')
year = np.timedelta64(2026,'Y')
print(day)
print(month)
print(year)


#cretae a numpy array which is timedelta type
arr=np.array([1,2,3],dtype='timedelta64[D]')
print(arr)
print(type(arr))

#in an organization the employees are working in shift manner , the shift times are 8hrs, 12hrs and 6hrs
#sometimes the employees are working in double shifts . Write a numpy program no of shifts required to
#finish 72hrs of project
shift =np.array([8,12,6], dtype='timedelta64[h]')
doushift =shift * 2
tpt=np.timedelta64(72,'h')
pct= tpt/shift
print("Original shift timings: ",shift)
print("Double shift timings: ",doushift)
print("NO of shifts required to complete",tpt,"hours project is ", pct)

#solution 2
num=72
arr=np.array([8,12,6])
res = num / arr
print(res)


#a student has 48 hours of the time to attempt an examination from current date.Find the date of the
#examination

