n=int(input("Enter a number : "))
c=0
r=1
while(r!=n):
    for i in range(1,n):
        if(r%i==0):
            c+=1
        
