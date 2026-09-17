n = int(input("enter the n value : "))
r=0
t=n
while (n>0):
    d=n%10
    r=r+d
    n=n//10
print("the sum of the digit is ",r)
