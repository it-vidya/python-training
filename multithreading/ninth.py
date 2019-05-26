from threading import Thread
store=[]
def producer():
    i=1
    while i<=1000:
        if len(store)<100:
            print("Producing item_"+str(i))
            store.append("item_"+str(i))
            i+=1
        else:
            print("Store is full,waiting for consumer!")
def consumer():
    i=1
    while i<=1000:
        if len(store)>0:
            print("Consuming "+store.pop(0))
            i+=1
        else:
            print("Store is empty,waiting for producer!")

t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()
