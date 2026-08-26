n = int(input("Enter the value of n : "))
count =0
i=2
while(i<=n) :
    if(n%i==0) :
        count = count+1
    i=i+1
if(count==1) :
    print(n," is a prime number")
else :
    print(n," is not a prime number")
