n=int(input("Enter a number : "))
count=0
s=str(n)
for i in range(0,len(s)):
    if(s[i]=='1'):
        count+=1
    else:
        continue
if(count%2==0):
    print("The given number ",n," is a Evil Number")
else:
    print("The given number ",n," is not a Evil Number")
