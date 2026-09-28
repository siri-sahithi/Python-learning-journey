n=int(input("enter a number : "))
s=n*n
c=str(n)
b=int('1'+len(c)*'0')
c=str(s//b)+str(s%b)
value=int(c)
print(value)
if(n==value):
    print("The given number ",n," is a Kaprekar number")
else:
    print("The given number ",n," is not a Karprekar number")
