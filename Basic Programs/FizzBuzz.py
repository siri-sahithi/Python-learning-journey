n=int(input("Enter a number : "))
if(n%3==0):
    if(n%5==0):
        print("FizzBuzz")
    else:
        print("Fizz")
elif(n%5==0):
    print("Buzz")
