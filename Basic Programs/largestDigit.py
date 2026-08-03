n = int(input("enter the number : "))
l=0
while(n!=0):
    d=n%10
    if(d>l) :
      l=d
    n=n//10
print(l)
