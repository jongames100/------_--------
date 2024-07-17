import threading

counter_lock=threading.Lock()

def MyThread ():
    global count
    for j in range (1000000):
        with counter_lock:
            count+=1

def MyThread2 ():
    global count
    for i in range(1000000):
        with counter_lock:
            count-=1

count=0
thread = threading.Thread(target=MyThread)
thread2 = threading.Thread(target=MyThread2)
thread.start()
thread2.start()
thread.join()
thread2.join()
print("count= ",count)