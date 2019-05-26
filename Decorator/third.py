class person:
    nationality="Indian"
    def sayhi(obj):
        print("Hi "+obj.fname+" "+obj.lname)
    def __init__(obj,fname,lname):
        obj.fname=fname
        obj.lname=lname

def demo():
    print("This is demo!!!")
data="Hello World"
