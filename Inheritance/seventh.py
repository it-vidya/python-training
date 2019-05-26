class person:
    nationality="Indian"
    def sayhi(self):
            print("HI "+self.fname)
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class employee(person):
    org="Oracle"
    def work(self):
        print(self.fname+" is working!")
    def __init__(self,fname,lname,eid,dept):
        person.__init__(self,fname,lname)
        self.eid=eid
        self.dept=dept
class student(person):
    inst="Demo University"
    def study(self):
        print(self.fname+" is studying!")
    def __init__(self,fname,lname,sid,stream):
        person.__init__(self,fname,lname)
        self.sid=sid
        self.stream=stream
class Intern(employee,student):
    def __init__(self,fname,lname,sid,stream,eid,dept):
        student.__init__(self,fname,lname,sid,stream)
        employee.__init__(self,fname,lname,eid,dept)
e1=Intern("Sachin","Tendulkar",7,"sports",10,"batting")
e1.sayhi()
e1.study()
e1.work()
print(e1.nationality,e1.inst,e1.org)
print(e1.__dict__)
print(Intern.__bases__)
