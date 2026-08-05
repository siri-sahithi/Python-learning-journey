n1=0
n2=1
a=int(input("enter the number of fibonacci number do you want : "))
c=0
print(n1,n2,end=" ")
while(c!=a):
    c+=1
    sum=n1+n2
    print(sum,end=" ")
    n1=n2
    n2=sum
   
   
