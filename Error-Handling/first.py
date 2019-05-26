try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=a/b
    print("Result: ",c)
except ZeroDivisionError as e:
    print(e)
print("Some other independant task!")
