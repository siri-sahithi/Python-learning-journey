n=int(input("Enter the value : "))
c1,c2=0,0
while(n!=0) :
    d=n%10
    if(d%2==0):
        c1+=1
    else :
        c2+=1
    n=n//10
print("the even count is ",c1);
print("the odd count is ",c2);
