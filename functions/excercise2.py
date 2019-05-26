products=[
    {"pid":"1001","name":" millet ","brand":"Aashirwad","category":"grocery  ","rating":"5"},
    {"pid":"1002","name":" grain  ","brand":"Patanjali","category":"grocery  ","rating":"3"},
    {"pid":"1003","name":" flour  ","brand":"Aashirwad","category":"grocery  ","rating":"4"},
    {"pid":"1004","name":" belt   ","brand":"Bulchi   ","category":"accessory","rating":"4"},
    {"pid":"1005","name":" cap    ","brand":"Levis    ","category":"accessory","rating":"2"},
    {"pid":"1006","name":" bread  ","brand":"Britannia","category":"grocery  ","rating":"4"},
    {"pid":"1007","name":" pulse  ","brand":"Aashirwad","category":"grocery  ","rating":"5"},
    {"pid":"1008","name":" plate  ","brand":"Milton   ","category":"dinning  ","rating":"5"},
    {"pid":"1009","name":" perfume","brand":"Setwet   ","category":"accessory","rating":"1"},
    {"pid":"1010","name":" butter ","brand":"Amul     ","category":"grocery  ","rating":"5"},
    {"pid":"1011","name":" oat    ","brand":"Saffola  ","category":"grocery  ","rating":"3"},
    {"pid":"1012","name":" shampoo","brand":"Patanjali","category":"beauty   ","rating":"3"}
]

print("\nsorted list as per brand :--\n")
products.sort(key=lambda c1:c1["brand"])
for d in products:
    print("| {pid} | {name} | {brand} | {category} | {rating} |".format(**d))

print("\nsorted list as per rating :--\n")
products.sort(reverse=True, key=lambda c1:c1["rating"])
for d in products:
    print("| {pid} | {name} | {brand} | {category} | {rating} |".format(**d))

print("\nsorted list as per name :--\n")
products.sort(key=lambda c1:c1["name"])
for d in products:
    print("| {pid} | {name} | {brand} | {category} | {rating} |".format(**d))
