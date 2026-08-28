import math
n = int(input("enter the n value : "))
r=0
t=n
while (n>0):
    d=n%10
    r=r+math.factorial(d)
    n=n//10
if(t==r):
    print(t," is a Strong number")
else :
    print(t," is not a Strong number")
