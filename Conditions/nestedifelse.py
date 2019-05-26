a=input("Enter number:")
b=input("Enter number:")
c=input("Enter number:")
print(type(a))
print(type(b))
print(type(c))
if a>b:
    if a>c:
        print("A is greater!")
    else:
        print("C is greater!")
else:
    if b>c:
        print("B is greater!")
    else:
        print("C is greater!")
