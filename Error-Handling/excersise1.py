try:
    names={"sachin":"sachin@icc","saurav":"bcci","rahul":"wall"}
    name=input("Enter name:")
    passd=input("Enter password:")
    if name in names and names[name]==passd:
        print("Welcome "+name)
    else:
        raise NameNotFound
except NameNotFound as e:
    print(e,type(e))
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
