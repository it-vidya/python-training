class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(obj):
        print("Hi "+obj.fname+" "+obj.lname)
p1=person()
p1.fname="Sachin"
p1.lname="Tendulkar"
p2=person()
p2.fname="Rahul"
p2.lname="Dravid"
person.sayhi(p1)
person.sayhi(p2)
p1.sayhi()# translated to person.sayhi(p1)
p2.sayhi()# translated to person.sayhi(p2)
