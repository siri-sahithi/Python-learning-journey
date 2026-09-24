n=int(input("Enter the number : "))
number1=str(n)+str(n*2)+str(n*3)
print(number1)
l=['1','2','3','4','5','6','7','8','9']
for i in range(0,len(number1)):
    if number1[i] in l:
        l.remove(number1[i])
    else:
        continue
if len(l)==0:
    print("The given number,"number1,"Fasinating number")
else:
    print("The given number,"number1," is not a fascinating Number")
'''
for i in range(0,len(number1)):
    for j in range(0,len(l)):
        if(number1[i] in l):
            l.remove(number1[i])
        else:
            continue
if l==[]:
    print("Fasinating number")
else:
    print("Not a fascinating Number")
'''
