n = int(input("enter the n value : "))
r=0
t=n
while (n>0):
    d=n%10
    r=r*10+d
    n=n//10
if (r==t):
    print( t," is a palindrome number")
else :
     print( t," is not a palindrome number")
