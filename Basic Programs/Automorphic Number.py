n=int(input("Enter the number : "))
s=n**2
d=s%10
r=n%10
if(d==r):
    print("The number ",n," is a Automorphic Number")
else:
    print("The number ",n," is not a Automorphic Number")
