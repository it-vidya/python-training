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
d1.sort(reverse=True,key=myorder)
for d in d1:
    print(d)
