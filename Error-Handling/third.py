try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=a/b
    print(z)#error
    print("Result: ",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Please enter numreic value!")
except Exception as e:
    print("This is generic error handler !",e.__class__.__name__)
print("Some other independant task!")
