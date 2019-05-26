from threading import Thread
def demo(name):
    for i in range(1,101):
        print(str(i)+name)


t1=Thread(target=demo,args=["Sachin"])
t2=Thread(target=demo,args=["Rahul"])
t3=Thread(target=demo,args=["Saurav"])
t1.start()
t2.start()
t3.start()
