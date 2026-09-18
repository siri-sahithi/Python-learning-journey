n=int(input("Enter the number : "))
t,sum,mul=n,0,1
while(n!=0):
    d=n%10
    sum+=d
    mul*=d
    n=n//10
if(sum==mul):
    print("The give number ",t,"is a Spy number")
else :
    print("The give number ",t," is not a Spy number")
