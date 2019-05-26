marks=input("Enter the marks obtained : ")
if marks>=0 and marks<=100:
    if marks>=0 and marks<=39:
        print("Fail")
    elif marks>=40 and marks<=59:
        print("Third")
    elif marks>=60 and marks<=79:
        print("second")
    else:
        print("First")
else:
    print("invalid input")
