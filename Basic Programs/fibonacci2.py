n=int(input("Enter the value of a : "))
n1=0
n2=1
next=n2
print(n1,n2,end=" ")
c=2
while(n!=c):
    n1,n2=n2,next
    print(next,end=" ")
    c+=1
    next=n2+n1
        
