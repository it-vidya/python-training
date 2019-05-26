#variable length args
def add(*a):
    print(a,type(a))
add()
add(1,2)
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5)
