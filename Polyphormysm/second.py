class Container:
    def __init__(self,itemList):
        self.itemList=itemList
    def __add__(self,other):
        itemList=self.itemList+other.itemList
        c=Container(itemList)
        return c
    def __lt__(self,other):
        return len(self.itemList)<len(other.itemList)
c1=Container(["item1","item2","item3"])
c2=Container(["item4","item5"])
c3=c1+c2
print(c1.itemList)
print(c2.itemList)
print(c3.itemList)
print(c1>c2)#True
print(c1<c2)#False
print(c1>c3)#False
