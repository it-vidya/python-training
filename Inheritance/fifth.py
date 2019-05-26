##Multilevel Inheritancea
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
class manager(employee):
    def __init__(self,fname,lname,dept,eid,reportees):
        employee.__init__(self,fname,lname,dept,eid)
        self.reportees=reportees
    def manage(self):
        print(self.fname+" is managing!")

e1=manager("Sachin","Tendulkar","sports","007",[])
e1.sayhi()
e1.work()
e1.manage()
print(e1.nationality)
print(e1.__dict__)
