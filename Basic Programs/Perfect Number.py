n=int(input("Enter the number : "))
total=0
for i in range(1,n+1):
    if(n%i==0 and i!=n):
            total+=i
            print(i)
if(total==n):
    print("The given number ",n," is a Perfect number")
else:
    print("The give number ",n," is not a Perfect number")
