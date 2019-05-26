def sayhi(**k):
    print("Hi "+k["name1"]+", "+k["name2"]+" and "+k["name3"])

d={"name3":"Sachin","name2":"Saurav","name1":"Rahul","name4":"Virat"}
sayhi(**d)
