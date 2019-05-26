class person:
    team="India"
p1=person()
print(type(p1))
p1.fname="Sachin"
p1.lname="Tendulkar"
print(p1.fname,p1.lname,p1.team,p1.__class__.team)

p2=person()
print(type(p2))
p2.fname="Rahul"
p2.lname="Dravid"
p2.team="Australia"
print(p2.fname,p2.lname,p2.team,p2.__class__.team)
