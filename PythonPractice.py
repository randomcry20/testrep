import threading 
import time

#we can give access to only 5 threads
semaphore=threading.BoundedSemaphore(value=2)

#semaphores will restrict the access of resources to a specified number of threads!
def resource(thread_number):
    print(f"{thread_number} is trying to access")
    semaphore.acquire()
    print(f"{thread_number} has been granted access")
    time.sleep(5)
    print(f"{thread_number} is being release now!")
    semaphore.release()

for x in range(1, 11):
    t=threading.Thread(target=resource, args=(x,))
    t.start()
    time.sleep(2)