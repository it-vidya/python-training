class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def setValues(obj,f,l):
        obj.fname=f
        obj.lname=l
p1=person()
person.setValues(p1,"Sachin","Tendulkar")
p2=person()
person.setValues(p2,"Rahul","Dravid")
p1.sayhi()
p2.sayhi()
