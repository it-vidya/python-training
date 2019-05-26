from threading import Thread,activeCount
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        # self.setName(name)
    def run(self):
        for i in range(1,21):
            print(str(i)+self.getName())
t1=MyThread()
t2=MyThread()
t3=MyThread()
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())
