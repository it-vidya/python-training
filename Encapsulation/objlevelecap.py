class person:
    pass
p1=person()
print(type(p1))
#Object level encapsulation
p1.fname="Sachin"
p1.lname="Tendulkar"
print(p1.fname,p1.lname)

p2=person()
print(type(p2))
#Object level encapsulation
p2.fname="Rahul"
p2.lname="Dravid"
p2.team="India"
print(p2.fname,p2.lname,p2.team)
