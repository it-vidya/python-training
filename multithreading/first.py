from threading import Thread
def demo1():
    for i in range(1,101):
        print(str(i)+"Sachin")

def demo2():
    for i in range(1,101):
        print(str(i)+"Rahul")

def demo3():
    for i in range(1,101):
        print(str(i)+"Saurav")

t1=Thread(target=demo1)
t2=Thread(target=demo2)
t3=Thread(target=demo3)
t1.start()
t2.start()
t3.start()
