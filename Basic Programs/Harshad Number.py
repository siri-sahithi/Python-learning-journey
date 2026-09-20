n=int(input("Enter a number : "))
t,s=n,0
while(n!=0):
    d=n%10
    s+=d
    n=n//10
print(s)
if(t%s==0):
    print("The given number ",t," is a Harshad number")
else:
    print("The given number ",t," is not a Harshad number")
