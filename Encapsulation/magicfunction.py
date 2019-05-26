#Magic Function
class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
p1=person("Sachin","Tendulkar")
p2=person("Rahul","Dravid")
p1.sayhi()
p2.sayhi()
