def demo(a):
    def inner():
        print("This is inner!")
        a()#a is the decoratede function
        print("Inner function finished execution")
    return inner

@demo
def sayhi():
    print("Hi All")


sayhi()
