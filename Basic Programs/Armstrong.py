n = int(input("enter the n value : "))
r=0
t=n
while (n>0):
    d=n%10
    r=r+(d*d*d)
    n=n//10
if(t==r):
    print(t," is a Arm strong number")
else :
    print(t," is not a Arm Strong number")
