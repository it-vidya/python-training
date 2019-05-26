class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
p1=person("Sachin","Tendulkar")
print(getattr(p1,"fname"))
print(getattr(person,"nationality"))
setattr(p1,"team","India")
print(getattr(p1,"team"))
print(hasattr(p1,"team"))
delattr(p1,"team")
print(hasattr(p1,"team"))
