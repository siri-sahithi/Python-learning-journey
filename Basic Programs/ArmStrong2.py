n=int(input("Enter a number : "))
t,s=n,0
while(n!=0):
    d=n%10
    s+=d**3
    n=n//10
if(t==s):
    print("The given number is a Arm Stronga number")
else:
    print("The given number is not a Arm Strong Number")
