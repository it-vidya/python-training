class person:#parent, super , base
    nationality="Indian"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class employee(person):#child,sub,derived
    org="Oracle"
    def work(self):
        print(self.fname+" is working!")

e1=employee("Sachin","Tendulkar")
e1.sayhi()
print(e1.nationality)
