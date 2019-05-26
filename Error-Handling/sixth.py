try:
    data=(1,2,3,4,435,43,543,543,543)
    it=data.__iter__()
    print(type(it))
    while True:
        print(it.__next__())
except StopIteration as e:
    pass
