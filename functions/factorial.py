def factorial(num):
    factorial = 1
    msg=""
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(num,0,-1):
            factorial = factorial*i
            msg+=str(i)+"*"
    print(msg,factorial)

factorial(5)
