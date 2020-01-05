# python-training

##fork-test

ASK USER TO ENTER A NUMBER AND FIND IT IS PRIME OR NOT

Assuming 1 may was wednesday ask user to enter a valid date(1-31)
and print day of the week on that date.`

find factorial of a number

'''
*
**
***
***
**
*
  *
 **
***
***
 **
  *
  
     P
    Py
   Pyt
  Pyth
 Pytho
Python
'''

def sayHi(name1,name2="Yuvraj"):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin")
sayHi("Sachin","Saurav")



from Virtual Classroom 55 to All Participants:
def sayHi():
    print("Hi All")
    
sayHi()
sayHi()
sayHi()
from Virtual Classroom 55 to All Participants:
def sayHi(name1,name2):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin","Rahul")
sayHi("Saurav","Rahul")
sayHi("Sachin","Saurav")
from Virtual Classroom 55 to All Participants:
#parameterised function
def sayHi(name1,name2):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin","Rahul")
sayHi("Saurav","Rahul")
sayHi("Sachin","Saurav")
from Virtual Classroom 55 to All Participants:
#parameterised function
def __add__(a,b):
    print(a+b)
    
__add__(1,2)
__add__(10,20)
__add__(100,200)
from Virtual Classroom 55 to All Participants:
#return type function
def add(a,b):
    return a+b
    
result=add(1,2)
print("Result: ",result)
res=add(
            add(10,20),
            add(100,200)
            )
print("Result: ",res)
from Jainendra to Host (privately):
Traceback (most recent call last):
  File "parameterised_function.py", line 4, in <module>
    sayHi("Sachin","Rahul","Ravi")
TypeError: sayHi() takes exactly 2 arguments (3 given)
[jkumar@localvm functions]$ python parameterised_function.py 
Hi Sachin and Rahul
Traceback (most recent call last):
  File "parameterised_function.py", line 5, in <module>
    sayHi("Saurav")
TypeError: sayHi() takes exactly 2 arguments (1 given)
from Virtual Classroom 55 to All Participants:
#parameterised function
def sayHi(name1,name2):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin","Rahul","Yuvraj")#Error
#TypeError: sayHi() takes 2 positional arguments but 3 were given
from Virtual Classroom 55 to All Participants:
#parameterised function
def sayHi(name1,name2):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin")#Error
#TypeError: sayHi() missing 1 required positional argument: 'name2'
from Virtual Classroom 55 to All Participants:
#default args
def sayHi(name1,name2="Yuvraj"):
    print("Hi "+name1+" and "+name2)
    
sayHi("Sachin")
sayHi("Sachin","Saurav")
from Virtual Classroom 55 to All Participants:
def sayHi(name1="Sachin",name2):#error
    print("Hi "+name1+" and "+name2)
from Virtual Classroom 55 to All Participants:
#positional args
def sayHi(name1,name2,name3):
    print("Hi "+name1+" and "+name2+" and "+name3)
    
sayHi("Sachin","Saurav","Rahul")
from Virtual Classroom 55 to All Participants:
#positional args
def sayHi(name3,name1,name2):
    print("Hi "+name1+" and "+name2+" and "+name3)
    
sayHi("Sachin","Saurav","Rahul")

#keyworded args
def sayHi(name1,name2,name3):
    print("Hi "+name1+" and "+name2+" and "+name3)
    
	
sayHi(name2="Sachin",name3="Saurav",name1="Rahul")

#variable length args
def add(*a):
    print(a,type(a))
add()    
add(1,2)
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5)

#variable length keyword args
def sayhi(**k):
    print(k,type(k))
sayhi(name1="Sachin")
sayhi(name1="Sachin",name2="Rahul")
sayhi(name1="Sachin",name2="Rahul",name3="Saurav")
sayhi(name1="Sachin",name2="Rahul",name3="Saurav",name4="Yuvraj")


#Generic Function
def sayhi(*a,**k):
    print(a,k)
sayhi()
sayhi("Sachin")
sayhi(name="Sachin")
sayhi("Sachin","Rahul")
sayhi("Sachin","Rahul",name3="Saurav")
sayhi("Sachin","Rahul",name3="Saurav",name4="Yuvraj")

def sayhi(name1,name2,name3):
    print("Hi "+name1+", "+name2+" and "+name3)
    
li=["Sachin","Saurav","Rahul"]
# sayhi(li[0],li[1],li[2])
sayhi(*li)

def sayhi(name1,name2,name3):
    print("Hi "+name1+", "+name2+" and "+name3)
    
d={"name3":"Sachin","name2":"Saurav","name1":"Rahul"}
sayhi(**d)




def sayhi(**k):
    print("Hi "+k["name1"]+", "+k["name2"]+" and "+k["name3"])
    
d={"name3":"Sachin","name2":"Saurav","name1":"Rahul","name4":"Virat"}
sayhi(**d)



#FOO
#All values of all datatypes are stored in heap.
def sayhi():
    print("Hi All!!!")
    
print(type(sayhi))
#Function is a datatype in python
from Virtual Classroom 55 to All Participants:
#FOO
#All values of all datatypes are stored in heap.
def sayhi():
    print("Hi All!!!")
    
demo=sayhi
print(type(demo))
#Function is a datatype in python
from Virtual Classroom 55 to All Participants:
def sayhi():
    print("Hi All!!!")
    
demo=sayhi
print(type(demo))
demo()
demo()
demo()
from Virtual Classroom 55 to All Participants:
#FOO
#All values of all datatypes are stored in heap.
def sayhi():
    return "Hi All!!!"
    
demo=sayhi#reference of sayhi is passed to demo
print(type(demo))
#Function is a datatype in python
from Virtual Classroom 55 to All Participants:
#FOO
#All values of all datatypes are stored in heap.
def sayhi():
    return "Hi All!!!"
demo=sayhi()#return of sayhi is passed to demo
print(type(demo))
#Function is a datatype in python


#scope of variables
#nested function
def outer():
    print("This is outer!")
    def inner():
        print("This is inner!")
    inner()
        
outer()



local variables of a function are deleted when the function finishes execution.
'''
from Virtual Classroom 55 to All Participants:
#scope of variables
#nested function
def outer():
    print("This is outer!")
    def inner():
        print("This is inner!")
    inner()
        
outer()
from Virtual Classroom 55 to All Participants:
#scope of variables
#nested function
#Lexical scoping
#nested function can read  the local variables of
#containing functions.
def outer():
    print("This is outer!")
    data="Hello World!"
    def inner():
        def innermost():
            print("This is innermost!")
            print(data)
        innermost()
        print("This is inner!")
    inner()
    
        
outer()
from Virtual Classroom 55 to All Participants:
data="Hello Universe"
def test():
    data="Hello World"
    print(data)
print(data)    
test()
print(data)
from Virtual Classroom 55 to All Participants:
data="Hello Universe"
def test():
    global data
    data="Hello World"
    print(data)
print(data)    
test()
print(data)
from Virtual Classroom 55 to All Participants:
def test():
    data="Hello World"
    def testinner():
        data="Hello City"
        print(data)
    print(data)    
    testinner()
    print(data)
test()
from Virtual Classroom 55 to All Participants:
data="Hello Universe"
def test():
    data="Hello World"
    def testinner():
        nonlocal data
        data="Hello City"
        print(data)
    print(data)    
    testinner()
    print(data)
print(data)
test()
print(data)

data="Hello Universe"
def test():
    data="Hello World"
    def testinner():
        nonlocal data
        data="Hello City"
        print("testinner: ",data)
    print("test:",data)    
    testinner()
    print("test:",data)
print("Global: ",data)
test()
print("Global: ",data)

from Virtual Classroom 55 to All Participants:
data="Hello Universe"
def test():
    data="Hello World"
    def testinner():
        global data
        data="Hello City"
        print("testinner: ",data)
    print("test:",data)    
    testinner()
    print("test:",data)
print("Global: ",data)
test()
print("Global: ",data)
from Virtual Classroom 55 to All Participants:
count=0
def hello():
    global count
    print (count)
    count+=1
hello()
hello()
hello()
hello()
hello()
from Virtual Classroom 55 to All Participants:
count=0
def hello():
    count+=1
    global count
    print (count)
    
def bye():
    global count
    count+=1000
hello()
hello()
hello()
bye()
hello()
hello()
from Virtual Classroom 55 to All Participants:
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print (count)
    inner()
    inner()
    inner()
    
outer()
from Virtual Classroom 55 to All Participants:
def outer():
    count=0
    global inner
    def inner():
        nonlocal count
        count+=1
        print (count)
    
    
outer()
inner()
inner()
inner()
from Virtual Classroom 55 to All Participants:
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print (count)
    return inner#reference of inner function is returned
    
    
hello =outer()
hello()
hello()
hello()
hello()

def outer():
    count=0
    global inner
    def inner():
        nonlocal count
        count+=1
        print (count)
    
    
outer()
inner()
inner()
inner()
from Virtual Classroom 55 to All Participants:
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print (count)
    return inner#reference of inner function is returned
    
    
hello =outer()
hello()
hello()
hello()
hello()
from Virtual Classroom 55 to All Participants:
#function returning nested function.
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print (count)
    return inner#reference of inner function is returned
    
    
hello =outer()
hello()
hello()
hi=outer()
hello()
hello()
hi()
hi()
hi()
hi()
from Virtual Classroom 55 to All Participants:
def demo():
    return 1
    print("Hello ")
    return 2
    
data=demo()
print(data)
from Virtual Classroom 55 to All Participants:
def demo():
    return {"a":1,"b":2}
    
data=demo()
print(data["a"])
print(data["b"])
from Virtual Classroom 55 to All Participants:
def demo():
    return [1,2]
    
data=demo()
print(data[0])
print(data[1])


def demo():
    return [1,2]
    
data=demo()
print(data[0])
print(data[1])
from Virtual Classroom 55 to All Participants:
#Closures
#function returning nested function.


from Virtual Classroom 55 to All Participants:
astring = "Hello world! World world World!"
print(len(astring))
print(astring.index("o"))
print(astring.index('o',5))#start searching from 5th index
print(astring.index('o',5,8))#8th is excluded
print(astring.count("l"))
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print (astring.endswith("d!"))
words = astring.split(" ")
print(words)
print(astring.find('o'))
print(astring.find('o',5))
print(astring.find('o',5,7))
print(astring.replace("World", "Python"))


temp = "Hello {fname} {lname} , welcome to {city}"
actData=temp.format(fname="Sachin" ,lname="Tendulkar" ,city= "Bengaluru")
print(temp)
print(actData)


temp = "Hello {} {} , welcome to {}"
li=[
    ["Sachin" ,"Tendulkar" , "Bengaluru"],
    ["Saurav" ,"Ganguly" , "Bengaluru"],
    ["Rahul" ,"Dravid" , "Kolkata"]
    ]
for d in li:
    print(temp.format(*d))

	
temp = "Hello {} {} , welcome to {}"
actData=temp.format("Sachin" ,"Tendulkar" , "Bengaluru")
print(temp)
print(actData)
temp = "Hello {fname} {lname} , welcome to {city}"
actData=temp.format(fname="Sachin" ,lname="Tendulkar" ,city= "Bengaluru")
print(temp)
print(actData)
from Virtual Classroom 55 to All Participants:
temp = "Hello {} {} , welcome to {}"
li=[
    ["Sachin" ,"Tendulkar" , "Bengaluru"],
    ["Saurav" ,"Ganguly" , "Bengaluru"],
    ["Rahul" ,"Dravid" , "Kolkata"]
    ]
for d in li:
    print(temp.format(*d))

	
	
	temp = "Hello {fname} {lname} , welcome to {city}"
li=[
    {"city":"Bengaluru","fname":"Sachin" ,"lname":"Tendulkar" },
    {"city":"Bengaluru","fname":"Saurav" ,"lname":"Ganguly" },
    {"city":"Kolkata","fname":"Rahul" ,"lname":"Dravid" }
    ]
for e in li:
    print(temp.format(**e))
	
	
	
l=['a','b','c','d','e','f']
l2=[1,2,3,4]
print(len(l))
print(sum(l2)) 
print(max(l)) 
print(max(l2)) 
print(min(l) )
print(min(l2) )
l.append('g')
print("appended" , l)
l3=['h','i','j','k']
l.extend(l3)
print("After extending: ",l)
l.insert(2,'z')
print("After insertion: " ,l)
print("Removing:",l.pop(2))
print("Removing:",l.pop())
print("After popping: " , l)
l.remove('a')
print("After removing a: " , l)
l.reverse()
print("After reversing: ",l)
l.sort(reverse=True)  
print("After sorting: ",l)
print("count of a",l.count('a'))



def sayhi():
    return "Hi ALL!!!"
def demo(a):
    print("Datatype: ",type(a))
    a()
    a()
    a()

	
	#Functional programing
demo(sayhi)#reference of sayhi is passed
from Virtual Classroom 55 to All Participants:
li=['Python','Session','John','Alpha','Beta']
li.sort(reverse=True)
print(li)




d1=[
    {"fname":"Sachin","lname":"Tendulkar"},
    {"fname":"Saurav","lname":"Ganguly"}  ,
    {"fname":"Rahul","lname":"Dravid"},
    {"fname":"Yuvraj","lname":"Singh"},
    {"fname":"Anil","lname":"Kumble"},
    {"fname":"Harbhajan","lname":"Singh"}
    ]
def myorder(el):
        print("myorder called for "+el["fname"])
        return el["fname"]
d1.sort(reverse=False,key=myorder)
for d in d1:
    print(d)
	
#filtering
d1=[
    {"team":"India","fname":"Sachin","lname":"Tendulkar"},
    {"team":"India","fname":"Saurav","lname":"Ganguly"}  ,
    {"team":"India","fname":"Rahul","lname":"Dravid"},
    {"team":"India","fname":"Yuvraj","lname":"Singh"},
    {"team":"India","fname":"Anil","lname":"Kumble"},
    {"team":"India","fname":"Harbhajan","lname":"Singh"},
    {"team":"Australia","fname":"Rick","lname":"Ponting"},
    {"team":"Australia","fname":"Brett","lname":"Lee"},
    {"team":"Australia","fname":"Adam","lname":"Gilchrist"},
    {"team":"WIndies","fname":"Chris","lname":"Gayle"}
    ]
def myfilter(el):
    return el["team"]=="Australia"
newdata=filter(myfilter,d1)
print(type(newdata))
for d in newdata:
    print("{fname} {lname} {team}".format(**d))
	
	
	
#mapping
li=(22,32,24,34,43,32)
def mymap(el):
    return el/2
newdata = map(mymap,li)
print(type(newdata))
for n in newdata:
    print(n)
	

lambda name:"Hi "+name
from Virtual Classroom 55 to All Participants:
#Anonymous Function(Remove name)
#In line  Function(bring in same line , remove return keyword)
#Lambda Function
from Virtual Classroom 55 to All Participants:
'''
Rule1: function should contain only 1 line.
Rule2: that 1 line should be a return statement.
def sayhi(name):
    return "Hi "+name
    
lambda name: "Hi "+name
'''
from Virtual Classroom 55 to All Participants:
def add(a,b):
    return a+b
from Jainendra to Virtual Classroom 55 (privately):
lambda (a,b) : a+b
	
DAY3

class person:
    pass
    
p1=person()
print(type(p1))


    
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




class person:
    nationality="Indian"#Class level encapsulation
    def sayhi():
        print("Hi All!!!")
p1=person()
p1.fname="Sachin"
p1.lname="Tendulkar"
p2=person()
p2.fname="Rahul"
p2.lname="Dravid"
person.sayhi()


person.sayhi()


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

def setValues(obj,f,l):
    obj.fname=f
    obj.lname=l
class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
p1=person()
setValues(p1,"Sachin","Tendulkar")
p2=person()
setValues(p2,"Rahul","Dravid")
p1.sayhi()
p2.sayhi()

#Magic Function
class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
p1=person("Sachin","Tendulkar")
p2=person("Rahul","Dravid")
p1.sayhi()
p2.sayhi()


#Attributes(predefined)

class person:
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
p1=person("Sachin","Tendulkar")
print(getattr(p1,"fname"))
print(getattr(person,"nationality"))
setattr(p1,"team","India")
print(getattr(p1,"team"))
print(hasattr(p1,"team"))
delattr(p1,"team")
print(hasattr(p1,"team"))

class person:
    '''This is a demo class to understand oop'''
    nationality="Indian"#Class level encapsulation
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(obj,f,l):#initialiser,constructor
        obj.fname=f
        obj.lname=l
print(person.__name__)
print(person.__module__)
print(person.__doc__)
print(person.__dict__)
# print(person.__bases__)


Inheritance

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
print(e1.nationality)

Inheritance with constructor

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

##Constructor overriding
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

        self.fname=fname
        self.lname=lname
        self.dept=dept
        self.eid=eid

e1=employee("Sachin","Tendulkar","sports","007")
e1.sayhi()
e1.work()
print(e1.nationality)
print(e1.__d



#function overriding
#constructor overriding
#Constructor chaining:
#from the constructor of child class ,
#we should call the constructor of parent class.
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
        
e1=employee("Sachin","Tendulkar","sports","007")
e1.sayhi()
e1.work()
print(e1.nationality)
print(e1.__dict__)


##Multilevel Inheritance

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
    def manage():
        print(self.fname+" is managing!")
        
e1=manager("Sachin","Tendulkar","sports","007",[])
e1.sayhi()
e1.work()
e1.manage()
print(e1.nationality)
print(e1.__dict__)



##Hierarchial Inheritance
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


##Multi

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



#Function overloading
def add(a,b):
    return a+b
    
print(add(1,2))
print(add(1.11,2.22))
print(add("Hello "," World"))
print(add((1,2),(3,4)))
print(add([1,2],[3,4]))
from Virtual Classroom 55 to All Participants:
#Magic Function
class person:
    nationality="Indian"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return "{fname} {lname}".format(**self.__dict__)
    def __int__(self):
        return len(self.fname)+len(self.lname)
    def __float__(self):
        return len(self.fname)/len(self.lname)
        
p1=person("Sachin","Tendulkar")
print(str(p1))
print(int(p1))
print(float(p1))
from Virtual Classroom 55 to All Participants:
https://drive.google.com/open?id=0B6UFRQ0r5ie_MDhDRjJBUU5Qelk



class Container:
    def __init__(self,itemList):
        self.itemList=itemList
c1=Container(["item1","item2","item3"])
c2=Container(["item4","item5"])
print(c1.itemList)
print(c2.itemList)
# c3=c1+c2
from Virtual Classroom 55 to All Participants:
class Container:
    def __init__(self,itemList):
        self.itemList=itemList
    def __add__(self,other):
        itemList=self.itemList+other.itemList
        c=Container(itemList)
        return c
c1=Container(["item1","item2","item3"])
c2=Container(["item4","item5"])
c3=c1+c2
print(c1.itemList)
print(c2.itemList)
print(c3.itemList)


class Container:
    def __init__(self,itemList):
        self.itemList=itemList
    def __add__(self,other):
        itemList=self.itemList+other.itemList
        c=Container(itemList)
        return c
    def __lt__(self,other):
        return len(self.itemList)<len(other.itemList)
c1=Container(["item1","item2","item3"])
c2=Container(["item4","item5"])
c3=c1+c2
print(c1.itemList)
print(c2.itemList)
print(c3.itemList)
print(c1>c2)#True
print(c1<c2)#False
print(c1>c3)#False


##W mode
fo=open("mydata.txt","w")
fo.write("Hello Python \n")
fo.write("Hello Python \n")
fo.write("Hello Python \n")
fo.write("Hello Python \n")
fo.close()
#if file does not  exist "w" creates w file.
#if file exists "w" will overwrite old data.

fo=open("mydata.txt","r")
data =fo.read()
print(data)
fo.close()
#if file does not  exist "r" errors out.
from Virtual Classroom 55 to All Participants:
fo=open("mydata.txt","r")
data =fo.read(20)
print(data)
fo.close()
#if file does not  exist "r" errors out.


fo=open("mydata.txt","r")
data =fo.read(10)#first 10 char
print(data)
data =fo.read(10)#next 10 char
print(data)
data =fo.read(10)#next 10 char
print(data)
fo.close()
#if file does not  exist "r" errors out.
from Virtual Classroom 55 to All Participants:
fo=open("mydata.txt","r")
data =fo.readline()#first line
print(data)
data =fo.readline()#second line
print(data)
data =fo.readline()#third line
print(data)
fo.close()
#if file does not  exist "r" errors out.



fo=open("mydata.txt","r")
for line in fo:
    print(line,end="")
fo.close()



fo=open("mydata.txt","rb")
for line in fo:
    print(line,end="")
fo.close()

fo=open("mydata.txt","rb")
print(fo.tell())
for line in fo:
    print(line.decode(),end="")
print(fo.tell())
print("Reading Again: ")
fo.seek(-4,1)
print(fo.tell())
for line in fo:
    print(line.decode(),end="")
print(fo.tell())    
    
fo.close()



#########################DAY 4 #############################


a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
c=a/b 
print("Result: ",c)
print("Some other independant task!")
from Virtual Classroom 55 to All Participants:
https://www.apachefriends.org/download.html
from Virtual Classroom 55 to All Participants:
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=a/b 
    print("Result: ",c)
except ZeroDivisionError as e:
    print(e)
print("Some other independant task!")
_________________________________________________________________________

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=a/b 
    print("Result: ",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Please enter numreic value!")
print("Some other independant task!")

_________________________________________________________________________
## Geeric handler should be kept at last always

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    c=a/b 
    print(z)#error
    print("Result: ",c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Please enter numreic value!")
except Exception as e:
    print("This is generic error handler !",e.__class__.__name__)
print("Some other independant task!")

_________________________________________________________________________

##Manually Raise Error
try:
    names=["Sachin","Saurav","Rahul","Yuvraj"]
    name=input("Enter name:")
    if name not in names:
        raise NameError("Name not found in list..")
    print("Welcome "+name)
except NameError as e:
    print("This is NameError handler!")
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
__________________________________________________________________________

#custom error
class NameNotFound(Exception):
    def __init__(self,msg="Name not Found in list!"):
        Exception.__init__(self,msg)
try:
    names=["Sachin","Saurav","Rahul","Yuvraj"]
    name=input("Enter name:")
    if name not in names:
        raise NameNotFound
    print("Welcome "+name)
except NameNotFound as e:
    print(e)
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")

_____________________________________________________________________________

try:
    names={"sachin":"sachin@icc","saurav":"bcci","rahul":"wall"}
    name=input("Enter name:")
    passd=input("Enter password:")
    if name in names and names[name]==passd:
        print("Welcome "+name)
    else:
        raise NameNotFound
except NameNotFound as e:
    print(e,type(e))
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
_______________________________________________________________________________
##Iterator

data="Hello World!"
for d in data:
    print(d)
from Virtual Classroom 55 to All Participants:
data="Hello World!"
it=data.__iter__()
print(type(it))
------------------------------------------------------------------------------

from Virtual Classroom 55 to All Participants:
data=[1,2,3,4]
it=data.__iter__()
print(type(it))

--------------------------------------------------------------------------------
#custom error
class NameNotFound(Exception):
    def __init__(self,msg="Name not Found in list!"):
        Exception.__init__(self,msg)
try:
    names={"sachin":"sachin@icc","saurav":"bcci","rahul":"wall"}
    name=input("Enter name:")
    passd=input("Enter password:")
    if name in names and names[name]==passd:
        print("Welcome "+name)
    else:
        raise NameNotFound
except NameNotFound as e:
    print(e,type(e))
except Exception as e:
    print("This is generic error handler !",e,e.__class__.__name__)
print("Some other independant task!")
from Virtual Classroom 55 to All Participants:
data="Hello World!"
for d in data:
    print(d)
from Virtual Classroom 55 to All Participants:
data="Hello World!"
it=data.__iter__()
print(type(it))
from Virtual Classroom 55 to All Participants:
data=[1,2,3,4]
it=data.__iter__()
print(type(it))
from Virtual Classroom 55 to All Participants:
data={}
it=data.__iter__()
print(type(it))
data={}
it=data.keys().__iter__()
print(type(it))
data={}
it=data.values().__iter__()
print(type(it))


------------------------------------------------------------------------------------------

data=[1,2,3,4,5]
it=data.__iter__()
print(type(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

_________________________________________________________________________________________

data={5,4,6,3,7,1}
it=data.__iter__()
print(type(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

_______________________________________________________________________________

try:
    data=(1,2,3,4,435,43,543,543,543)
    it=data.__iter__()
    print(type(it))
    while True:
        print(it.__next__())
except StopIteration as e:
    pass
	
	_______________________________________________________________________________
	
<class 'list_iterator'>
<class 'str_iterator'>
<class 'tuple_iterator'>
<class 'set_iterator'>
<class 'dict_keyiterator'>
<class 'range_iterator'>
'''

_________________________________________________________________________________________

Rules of Iteration (Iteration Protocol)
1)Every iterable class has an iterator class.
2)Every iterable class has __iter__() which creates and returns 
iterator object.
3)Every iterator has __next__() function , which returns 1 value at a time
 from the iterable.
4)after iteration is over __next__() function will raise  StopIteration error
'''
# range(10)
class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        obj= myrange_iter(self.n)
        return obj
        
class myrange_iter:
    def __init__(self,n):
        self.n=n
        self.start=0
    def __next__(self):
        if self.start<self.n:
            self.start+=1
            return self.start
        else:
            raise StopIteration
    
for i in myrange(12):
    print(i)
	
_________________________________________________________________________

class myrange:
    def __init__(self,s,n,step):
        self.s=s
        self.n=n
        self.step=step
    def __iter__(self):
        obj= myrange_iter(self)
        return obj
        
class myrange_iter:
    def __init__(self,obj):
        self.s=obj.s
        self.n=obj.n
        self.step=obj.step
    def __next__(self):
        if self.s<self.n:
            self.s+=self.step
            return self.s
        else:
            raise StopIteration
    
for i in myrange(100,200,10):
    print(i)
	
_________________________________________________________________________________________

##Enhaced Itrator

def demo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    
it=demo()
for i in it:
    print("value = ",i)

_________________________________________________________________________________________

#Enhanced iterators
#Generator
#on demand value generation.
def demo():
    print("Going to yield 1")
    yield 1
    print("Yielded 1")
    yield 2
    print("Yielded 2")
    yield 3
    print("Yielded 3")
    yield 4
    print("Yielded 4")
    yield 5
    print("Yielded 5")
    yield 6
    print("Yielded 6")
    
it=demo()
print(type(it))
for i in it:
    print("for loop consumed value = ",i)
	
_________________________________________________________________________________________

#Enhanced iterators
#Generator
#on demand value generation.
def demo():
    print("Going to yield 1")
    yield 1
    print("Yielded 1")
    yield 2
    print("Yielded 2")
    yield 3
    print("Yielded 3")
    yield 4
    print("Yielded 4")
    yield 5
    print("Yielded 5")
    yield 6
    print("Yielded 6")
try:    
    it=demo()
    print(type(it))
    while True:
        print(it.__next__())
except StopIteration:
    pass
from Virtual Classroom 55 to All Participants:
#Enhanced iterators
#Generator
#on demand value generation.
def myrange(n):
    start=0
    while start<n:
        yield start
        start+=1
        
for i in myrange(10):
    print(i)
_________________________________________________________________________________________

#List Comprehension
#[ExprToBeAddedToList  loop  <condition> ]
print([i**2 for i in range(1,11) ])
from Virtual Classroom 55 to All Participants:
#List Comprehension
#[ExprToBeAddedToList  loop  <condition> ]
data = {i**2 for i in range(1,11) }
print(data,type(data))
from Virtual Classroom 55 to All Participants:
#List Comprehension
#[ExprToBeAddedToList  loop  <condition> ]
data = {i:i**2 for i in range(1,11) }
print(data,type(data))
from Virtual Classroom 55 to All Participants:
#List Comprehension
#[ExprToBeAddedToList  loop  <condition> ]
data = (i**2 for i in range(1,11) )
print(data,type(data))	
	
_________________________________________________________________________________________
li=[]
n=int(input("Enter number"))
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
        
print(li)


n=int(input("Enter number"))
def my(i):
    return n%i==0
print(list(filter(my,range(1,n+1))))


def my(i):
    return i**2
print(list(map(my,range(1,11))))
        
_________________________________________________________________________________________

d1=[
    {"team":"India","fname":"Sachin","lname":"Tendulkar"},
    {"team":"India","fname":"Saurav","lname":"Ganguly"}  ,
    {"team":"India","fname":"Rahul","lname":"Dravid"},
    {"team":"India","fname":"Yuvraj","lname":"Singh"},
    {"team":"India","fname":"Anil","lname":"Kumble"},
    {"team":"India","fname":"Harbhajan","lname":"Singh"},
    {"team":"Australia","fname":"Rick","lname":"Ponting"},
    {"team":"Australia","fname":"Brett","lname":"Lee"},
    {"team":"Australia","fname":"Adam","lname":"Gilchrist"},
    {"team":"WIndies","fname":"Chris","lname":"Gayle"}
    ]

	
	
	
	def demo(a):
    def inner():
        print("This is inner!")
    return inner
        
@demo        
def sayhi():
    print("Hi All")
    
        
sayhi()
sayhi()
sayhi()


def demo(a):
    def inner():
        print("This is inner!")
        a()#a is the decoratede function
        print("Inner function finished execution")
    return inner
        
@demo        
def sayhi():
    print("Hi All")
    
        
sayhi()



#Decorators:
#All decorators are closures
def demo(a):
    def inner(*t):
        print("This is inner!")
        a(*t)#a is the decoratede function
        print("Inner function finished execution")
    return inner
        
@demo        
def sayhi():
    print("Hi All")
    
    
@demo        
def sayhello(name):
    print("Hello "+name)    
    
    
sayhi()
sayhello("Sachin")


class person:
    nationality="Indian"
    def sayhi(obj):
        print("Hi "+obj.fname+" "+obj.lname)
    def __init__(obj,fname,lname):
        obj.fname=fname
        obj.lname=lname
        
def demo():
    print("This is demo!!!")
data="Hello World"

from first import person as p ,demo  as d
p1=p("Sachin","Tendulkar")
print(type(p1))
p1.sayhi()
d()



import osprint(os.listdir())#cwd# print(os.listdir(<path to any directory>))


import os
print(os.listdir())#cwd
# print(os.listdir(<path to any directory>))


import os
print(os.getcwd())
os.chdir("..")
print(os.getcwd())


import os
os.makedirs("test\\multiple\\levels")
os.removedirs("test\\multiple\\levels")
from Virtual Classroom 55 to All Participants:
os.remove("demo.txt")

import os
stat =os.stat('first.py') 
print(stat)
print(stat.st_atime)
print(stat.st_mtime)
print(stat.st_ctime)
print(stat.st_size)

import os
print(os.name)
os.system('echo "hi"')
os.system('dir')
os.system('python first.py')
os.system('calc.exe')


import os.path
filename="C:\Users\\TECHTRAININGBLR_IN\\Desktop\\Shashank\\Python Oracle\\Examples\\11SampleModules\\1os,sys\\os\\demo.py"
print("dirname", "=>", os.path.dirname(filename))
print("basename", "=>", os.path.basename(filename))

import os.path
filename="C:\\user\\demo.txt"
t=os.path.split(filename)
print("Dir: ",t[0])
print("File: ",t[1])



import os
file="C:\\User\\demo.txt"
print(os.path.exists(file))
print(os.path.isabs(file))
print(os.path.isdir(file))
print(os.path.isfile(file))
print(os.path.islink(file))

import os
# print(os.environ)
print(os.environ["PYTHONPATH"])
os.environ["User"]="root"
print(os.environ["User"])

import os
# print(os.environ)
print(os.environ["PYTHONPATH"])
os.environ["User"]="root"
print(os.environ["User"])
varPath="Users/$User/bin"
actPath=os.path.expandvars(varPath)
print(actPath)



import re
pattern = 'a*'
text = 'aaa'
match = re.search(pattern, text)
if match!=None:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print("found match: {} for pattern: {} ".format(text[s:e],p))
	
	
import re
pattern = 'a?'
text = 'aaa'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match!=None:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))


import re
pattern = '.'
text = 'abcd'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match!=None:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))

import re
pattern = 'a{5}'
text = 'aaaaaaaaabcd'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
else:
    print("No match found")

	
import re
pattern = 'a{5,7}'
text = 'aaaaaaaaaaaaabcd'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
else:
    print("No match found")
	
	
import re
pattern = '[a-z]'
text = 'xyza'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
else:
    print("No match found")
       
	   
import re
pattern = '[^a-z]'
text = 'abcdbcdbcbdbcbdbcbdbdxyzHelloSAdfsdfa'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
else:
    print("No match found")
	
	
_________________________________________________________________________________________

Day5
Multi threading

from threading import Thread
def demo1():
    for i in range(1,101):
        print(str(i)+"Sachin")
        
def demo2():
    for i in range(1,101):
        print(str(i)+"Rahul")
        
def demo3():
    for i in range(1,101):
        print(str(i)+"Saurav")
        
t1=Thread(target=demo1)
t2=Thread(target=demo2)
t3=Thread(target=demo3)
t1.start()
t2.start()
t3.start()
_________________________________________________________________________________________

from threading import Thread
def demo(name):
    for i in range(1,101):
        print(str(i)+name)
        
        
t1=Thread(target=demo,args=["Sachin"])
t2=Thread(target=demo,args=["Rahul"])
t3=Thread(target=demo,args=["Saurav"])
t1.start()
t2.start()
t3.start()

_________________________________________________________________________________________

from threading import Thread
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name
    def run(self):
        for i in range(1,101):
            print(str(i)+self.name)
            
        
t1=MyThread("Sachin")
t2=MyThread("Rahul")
t3=MyThread("Saurav")
t1.start()
t2.start()
t3.start()


from threading import Thread
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self,target=self.demo)
        self.name=name
    def demo(self):
        for i in range(1,101):
            print(str(i)+self.name)
            
        
t1=MyThread("Sachin")
t2=MyThread("Rahul")
t3=MyThread("Saurav")
t1.start()
t2.start()
t3.start()
_________________________________________________________________________________________
from threading import Thread,activeCount
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name
    def run(self):
        for i in range(1,21):
            print(str(i)+self.name)
            
        
t1=MyThread("Sachin")
t2=MyThread("Rahul")
t3=MyThread("Saurav")
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())

_________________________________________________________________________________________

from threading import Thread,activeCount
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        # self.setName(name)
    def run(self):
        for i in range(1,21):
            print(str(i)+self.getName())    
t1=MyThread()
t2=MyThread()
t3=MyThread()
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())

_________________________________________________________________________________________

from threading import Thread,activeCount,currentThread
def anyGlobalTask():
    t=currentThread()
    print("global task executed by: "+t.getName())
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.setName(name)
    def run(self):
        for i in range(1,21):
            anyGlobalTask()    
t1=MyThread("Sachin")
t2=MyThread("Saurav")
t3=MyThread("Rahul")
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())
for i in range(1,21):
    anyGlobalTask()

_________________________________________________________________________________________

#MainThread
print("Active: ",activeCount())
print("Exiting Mainthread!")
from Virtual Classroom 55 to All Participants:
from threading import Thread,activeCount
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.setName(name)
    def run(self):
        
        for i in range(1,101):
            print(str(i)+self.getName())
            if self.name == "Rahul" and i==5:
                t2.join()
                
t1=MyThread("Sachin")
t2=MyThread("Saurav")
t3=MyThread("Rahul")
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())
print("Exiting Mainthread!")

_________________________________________________________________________________________

from time  import sleep
sleep(1)
print("Hello World")
sleep(1)
print("Hello World")
sleep(2)
print("Hello World")
_________________________________________________________________________________________
from threading import Thread
from time import sleep
class MyThread(Thread):
    def __init__(self,name,delay):
        Thread.__init__(self)
        self.setName(name)
        self.delay=delay
    def run(self):
        for i in range(1,11):
            print(str(i)+self.getName())
            sleep(self.delay)
            
t1=MyThread("Sachin",1.5)
t2=MyThread("Saurav",1)
t3=MyThread("Rahul",0.5)
t1.start()
t2.start()
t3.start()


_________________________________________________________________________
from threading import Thread
from time import sleep
'''
Python  process waits for all non-daemon threads to finish execution.
It does not take care of daemon threads.
Once all non daemon threads have finished execution,
Python will exit even if daemon threads are still under excution.
'''
class MyThread(Thread):
    def __init__(self,name,delay):
        Thread.__init__(self)
        self.setName(name)
        self.delay=delay
    def run(self):
        for i in range(1,11):
            print(str(i)+self.getName())
            sleep(self.delay)
            
t1=MyThread("Sachin",1.5)
t2=MyThread("Saurav",1)
t3=MyThread("Rahul",0.5)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t3.start()
_________________________________________________________________________________________

from threading import Thread,activeCount
class MyThread(Thread):
    log=open("output.log","wb")
    def __init__(self,inp):
        Thread.__init__(self)
        self.inp=inp
    def run(self):
        for line in self.inp:
            MyThread.log.write(line)
        self.inp.close()
        
t1=MyThread(open("file1.txt","rb"))
t2=MyThread(open("file2.txt","rb"))
t1.start()
t2.start()
t1.join()
t2.join()
MyThread.log.close()
_________________________________________________________________________________________
from threading import Thread,Lock
#mutex
class MyThread(Thread):
    log=open("output.log","wb")
    lock=Lock()
    def __init__(self,inp):
        Thread.__init__(self)
        self.inp=inp
    def run(self):
    
        #code to connect to db
        #should be written outside lock.
        MyThread.lock.acquire()
        for line in self.inp:
            MyThread.log.write(line)
        self.inp.close()
        MyThread.lock.release()
        
t1=MyThread(open("file1.txt","rb"))
t2=MyThread(open("file2.txt","rb"))
t1.start()
t2.start()
t1.join()
t2.join()
MyThread.log.close()
_________________________________________________________________________________________
from threading import Thread, Lock
def producer(lock, upper):
    global indexProducer
    while indexProducer < upper+1:
        lock.acquire()
        if len(myList) < 4:
            myString="item_" + str(len(myList))
            myList.append(myString)
        else:
            print("Length ",len(myList), "Skipping a produce")
        lock.release()
        print("Pushed ",indexProducer)
        indexProducer+=1
        
def consumer(lock, upper):
    global indexConsumer
    while indexConsumer < upper+1:
        lock.acquire()
        if len(myList) > 0:
            myString=myList.pop(0)
        lock.release()
        print("Popped ", indexConsumer)
        indexConsumer+=1
myList = []
lock = Lock()
indexProducer = 1
indexConsumer = 1
    
t1=Thread(target=producer, args=[lock, 10])
t2=Thread(target=consumer, args=[lock, 10])
t1.start()
t2.start()

_________________________________________________________________________________________

from threading import Thread
store=[]
def producer():
    i=1
    while i<=1000:
        if len(store)<100:
            print("Producing item_"+str(i))
            store.append("item_"+str(i))
            i+=1
        else:
            print("Store is full,waiting for consumer!")
def consumer():
    i=1
    while i<=1000:
        if len(store)>0:
            print("Consuming "+store.pop(0))
            i+=1
        else:
            print("Store is empty,waiting for producer!")
            
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()
_________________________________________________________________________________________
import sys
sys.stdout=open("output.log","w")
from threading import Thread
store=[]
def producer():
    i=1
    while i<=1000:
        if len(store)<100:
            print("Producing item_"+str(i))
            store.append("item_"+str(i))
            i+=1
        else:
            print("Store is full,waiting for consumer!")
def consumer():
    i=1
    while i<=1000:
        if len(store)>0:
            print("Consuming "+store.pop(0))
            i+=1
        else:
            print("Store is empty,waiting for producer!")
            
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()
_________________________________________________________________________________________

from threading import Thread,Condition
c=Condition()
import sys
sys.stdout=open("output.log","w")
store=[]
def producer():
    i=1
    while i<=1000:
        c.acquire()
        if len(store)<100:
            print("Producing item_"+str(i))
            store.append("item_"+str(i))
            i+=1
        else:
            print("Store is full,waiting for consumer!")
            c.wait()
        c.release()
def consumer():
    i=1
    while i<=1000:
        c.acquire()
        if len(store)>0:
            print("Consuming "+store.pop(0))
            i+=1
        else:
            print("Store is empty,waiting for producer!")
            c.wait()
        c.release()    
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()
_________________________________________________________________________________________

<users org="Oracle" session="Python"><user id="1"><fname>Sachin</fname><lname>Tendulkar</lname></user><user id="2"><fname>Saurav</fname><lname>Ganguly</lname></user><user id="3"><fname>Rahul</fname><lname>Dravid</lname></user></users>
from Virtual Classroom 55 to All Participants:
<users org="Oracle" session="Python">
    <user id="1">
        <fname>Sachin</fname>
        <lname>Tendulkar</lname>
    </user>
    <user id="2">
        <fname>Saurav</fname>
        <lname>Ganguly</lname>
    </user>
    <user id="3">
        <fname>Rahul</fname>
        <lname>Dravid</lname>
    </user>
</users>
from Virtual Classroom 55 to All Participants:
import xml.sax
class UserHandler( xml.sax.ContentHandler ):
    def startElement(self, tag, attributes):
        print('startElement called for ',tag)
    def characters(self, data):
            print('characters called for ',data)
    def endElement(self, tag):
        print('endElement called for ',tag)
Handler = UserHandler()    
# create an XMLReader
parser = xml.sax.make_parser()
# override the default ContextHandler
parser.setContentHandler( Handler )
parser.parse("second.xml")
from Virtual Classroom 55 to All Participants:
import xml.sax
class UserHandler( xml.sax.ContentHandler ):
    def startElement(self, tag, attributes):
        print('startElement called for ',tag)
    def characters(self, data):
        if data.strip():
            print('characters called for ',data)
    def endElement(self, tag):
        print('endElement called for ',tag)
Handler = UserHandler()    
# create an XMLReader
parser = xml.sax.make_parser()
# override the default ContextHandler
parser.setContentHandler( Handler )
parser.parse("first.xml")
   
   
   
   
   
   
from Virtual Classroom 55 to All Participants:
<users org="Oracle" session="Python">
    <user id="1">
        <fname>Sachin</fname>
        <lname>Tendulkar</lname>
    </user>
    <user id="2">
        <fname>Saurav</fname>
        <lname>Ganguly</lname>
    </user>
    <user id="3">
        <fname>Rahul</fname>
        <lname>Dravid</lname>
    </user>
</users>



_________________________________________________________________________________________

#!/usr/bin/python
import xml.dom.minidom
# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("first.xml")
root = DOMTree.documentElement#root
print(root.getAttribute("org"))
fnameList=root.getElementsByTagName("fname")
for fnameTag in fnameList:
    textNode=fnameTag.childNodes[0]
    print(textNode,textNode.data)
	
	#!/usr/bin/python
import xml.dom.minidom
# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("first.xml")
root = DOMTree.documentElement
userList=root.getElementsByTagName("user")
for user in userList:
    fname=user.getElementsByTagName("fname")[0]
    lname=user.getElementsByTagName("lname")[0]
    print(user.getAttribute("id") ,
            fname.childNodes[0].data,
            lname.childNodes[0].data)
			
			
_________________________________________________________________________________________

import json
fo=open("first.json","r")
data = json.load(fo)
print(type(data))
print(data)

------------------------
[{
        "id": 1,
        "fname": "Sachin",
        "lname": "Tendulkar"
    },
    {
        "id": 2,
        "fname": "Saurav",
        "lname": "Ganguly"
    },
    {
        "id": 3,
        "fname": "Rahul",
        "lname": "Dravid"
    },
    {
        "id": 4,
        "fname": "Yuvraj",
        "lname": "Singh"
    }
]

_________________________________________________________________________________________

import json
resp='''
    [
{"id":1,"fname":"Sachin","lname":"Tendulkar"},
{"id":2,"fname":"Saurav","lname":"Ganguly"},
{"id":3,"fname":"Rahul","lname":"Dravid"},
{"id":4,"fname":"Yuvraj","lname":"Singh"}
]
    '''
print(type(resp))
data = json.loads(resp)
print(type(data))
print(data)

__________________________________________________________________________
import json
data=[
{"id":1,"fname":"Sachin","lname":"Tendulkar"},
{"id":2,"fname":"Saurav","lname":"Ganguly"},
{"id":3,"fname":"Rahul","lname":"Dravid"},
{"id":4,"fname":"Yuvraj","lname":"Singh"}
]
json.dump(data,open("data.json","w"))

_________________________________________________________________________________________
import json
data=[
{"id":1,"fname":"Sachin","lname":"Tendulkar"},
{"id":2,"fname":"Saurav","lname":"Ganguly"},
{"id":3,"fname":"Rahul","lname":"Dravid"},
{"id":4,"fname":"Yuvraj","lname":"Singh"}
]
jsondata = json.dumps(data)
print(type(jsondata))
print(jsondata)

_________________________________________________________________________________________
Sachin:Tendulkar:Mumbai
Saurav:Ganguly:Kolkata
Rahul:Dravid:Bengaluru

import csv
fo= open('first.csv',"r") 
reader = csv.reader(fo, delimiter=':')
print(list(reader))
#list of list



[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes
[database]
User = hg
[chat]
User = demo
Port = 50022
ForwardX11 = no

import configparser
config = configparser.ConfigParser()
config.read('examples.ini')
print(config.sections())
print(config["database"]["User"])
print(config["database"]["Compression"])



import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
cursor.execute("""CREATE TABLE USER (
                 FNAME  CHAR(20) NOT NULL,
                 LNAME  CHAR(20))""")
db.close()


import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
fname=input("Enter fname: ")
lname=input("Enter lname: ")
query="Insert into USER VALUES('{}','{}')"
cursor.execute(query.format(fname,lname))
db.commit()
db.close()

import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
cursor.execute("Select * from user")
rows = cursor.fetchall()
print(rows)
db.close()
