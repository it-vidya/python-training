from threading import Thread,activeCount,currentThread
def anyGlobalTask():
    t=currentThread()
    print("global task executed by: "+t.getName())
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.setName(name)
    def run(self):
        for i in range(1,21):
            anyGlobalTask()
t1=MyThread("Sachin")
t2=MyThread("Saurav")
t3=MyThread("Rahul")
t1.start()
t2.start()
t3.start()
#MainThread
print("Active: ",activeCount())
for i in range(1,21):
    anyGlobalTask()
