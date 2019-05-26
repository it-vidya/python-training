li=[
    ("Sachin" ,"Ramesh","Tendulkar"),
    ("Saurav" ,"Ganguly"),
    ("Rahul" ,"Dravid"),
    ("Yuvraj" ,"Singh"),
    ("Anil" ,"Kumble")
    ]

li.sort(reverse=True,key=lambda el:el[-1])
for d in li:
    print(d)
