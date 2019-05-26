try:
    names=["Sachin","Saurav","Rahul","Yuvraj"]
    name=input("Enter name:")
    if name not in names:
        raise NameError("Name not found in list..")
    print("Welcome "+name)
except NameError as e:
    print("This is NameError handler!")
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
