year = int(input("Enter the year : "))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The given year",year," is a Leap year")
else:
    print("The given year",year," is not a Leap year")
