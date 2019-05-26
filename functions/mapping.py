#mapping
li=(22,32,24,34,43,32)
newdata = map(lambda el: (el*9/5)+32,li)
print(type(newdata))
for n in newdata:
    print(n)
print(list(map(lambda el: (el*9/5)+32,li)))
