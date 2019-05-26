class person:
    nationality="Indian"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
class employee(person):
    org="Oracle"
    def work(self):
        print(self.fname+" is working!")

e1=employee()
e1.fname="Sachin"
e1.lname="Tendulkar"
e1.sayhi()
e1.work()
print(e1.nationality)
