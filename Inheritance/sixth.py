####Hierarchial Inheritance
class person:
    nationality="Indian"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class employee(person):
    org="Oracle"
    def work(self):
        print(self.fname+" is working!")
    def __init__(self,fname,lname,dept,eid):
        person.__init__(self,fname,lname)
        self.dept=dept
        self.eid=eid
class student(person):
    def __init__(self,fname,lname,sid,stream):
        person.__init__(self,fname,lname)
        self.sid=sid
        self.stream=stream
    def study(self):
        print(self.fname+" is studying!")

e1=student("Sachin","Tendulkar","007","cricket")
e1.sayhi()
e1.study()
print(e1.nationality)
print(e1.__dict__)
