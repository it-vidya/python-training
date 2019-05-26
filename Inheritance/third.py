#function overriding
#constructor overriding
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
        self.fname=fname
        self.lname=lname
        self.dept=dept
        self.eid=eid

e1=employee("Sachin","Tendulkar","sports","007")
e1.sayhi()
e1.work()
print(e1.nationality)
print(e1.__dict__)
