class product:
    def sayhi(self):
        print(self.pid+"|"+self.name+"|"+self.category+"|"+self.rating)
    def __init__(obj,id,name,category,rating):#initialiser,constructor
        obj.pid=id
        obj.name=name
        obj.category=category
        obj.rating=rating
p1=product("1001","powder","cosmetics","4")
p2=product("1002","mirror","cosmetics","5")
p3=product("1003","bandaid","medical","3")
p4=product("1004","comb","cosmetics","3")
p5=product("1005","needle","sweing","4")
p6=product("1006","facecream","cosmetics","2")
p7=product("1007","belt","accessory","1")

print(p1.__dict__)
#i=int(input("Enter the choice of sorting\n 1.name\n2.rating"))
#if i==1 :
#    print("\nsorted list as per rating :--\n")
#    products.sort(reverse=True, key=lambda c1:c1["rating"])
#    for d in products:
#        print("| {pid} | {name} | {brand} | {category} | {rating} |".format(**d))
