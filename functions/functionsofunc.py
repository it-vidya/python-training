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
