def demo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

it=demo()
print(type(it))
for i in it:
    print(i-1)
