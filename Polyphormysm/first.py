class Container:
    def __init__(self,itemList):
        self.itemList=itemList
c1=Container(["item1","item2","item3"])
c2=Container(["item4","item5"])
print(c1.itemList)
print(c2.itemList)
# c3=c1+c2

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
