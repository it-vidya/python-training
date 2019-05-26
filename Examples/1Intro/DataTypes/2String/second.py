astring = "Hello world!"
print len(astring)
print astring.index("o")
print astring.index('o',5)
print astring.index('o',5,7)
print astring.count("l")
print astring.upper()
print astring.lower()
print astring.startswith("Hello")
print astring.endswith("d!")
words = astring.split(" ")
print words
print astring.find('o')
print astring.find('o',5)
print astring.find('o',5,7)
print astring.replace("World", "Python")
sub1='string'
print "i am a {0}".format(sub1)
print "Hi {title}. {name} , your discount coupon is {couponCode}".format(
title='Mr.' , name='Sachin',couponCode='QWQ342')
dict={'title':'Mr.' , 'name':'Rahul','couponCode':'QWQASD2'}
"Hi {title}. {name} , your discount coupon is {couponCode}".format(**dict)




