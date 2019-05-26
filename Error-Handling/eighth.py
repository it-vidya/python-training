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
newdata=filter(lambda el:el["team"].startswith("A"),d1)
for d in newdata:
    print("{team} {fname} {lname}".format(**d))
