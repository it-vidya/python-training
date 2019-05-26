#custom error
class NameNotFound(Exception):
    def __init__(self,msg="Name not Found in list!"):
        Exception.__init__(self,msg)
try:
    names=["Sachin","Saurav","Rahul","Yuvraj"]
    name=input("Enter name:")
    if name not in names:
        raise NameNotFound
    print("Welcome "+name)
except NameNotFound as e:
    print(e)
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
