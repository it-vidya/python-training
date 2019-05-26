def demo(a):
    def inner():
        print("This is inner!")
    return inner

@demo
def sayhi():
    print("Hi All")


sayhi()
sayhi()
sayhi()
