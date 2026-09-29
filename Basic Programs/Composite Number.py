n=int(input("Enter a number : "))
count=0
for i in range(1,n+1):
        if(n%i==0):
            count+=1
if(count>2):
    print("The given number ", n," is a Composite number")
else:
    print("The give number ", n," is not a Composite number")
            
