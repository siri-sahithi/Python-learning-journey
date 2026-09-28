n=int(input("Enter a number :"))
temp,s=n,0
m=n**2
while(m!=0):
    d=m%10
    s+=d
    m=m//10
if(temp==s):
    print("The given number ",temp," is a Neon Number")
else :
    print("The given number ",temp," is not a Neon Number")
