def sayhi(name1,name2,name3):
    print("Hi "+name1+", "+name2+" and "+name3)

li=["Sachin","Saurav","Rahul"]
# sayhi(li[0],li[1],li[2])
sayhi(*li)
