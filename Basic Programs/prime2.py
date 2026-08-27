n = int(input("Enter the last light of prime number sequence : "))
c=0
r=1
while (r!=n) :
    for i in range (1,n+1):
        if(n%i==0):
             c+=1
        if(c==2):
            print(n)
    r=r+1
    