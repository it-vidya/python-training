class person:
    '''This is a demo class to understand oop'''
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
print(person.__name__)
print(person.__module__)
print(person.__doc__)
print(person.__dict__)
# print(person.__bases__)
