import time
import thread

def printtime(name,iter,delay):
    count = 1
    while count <= iter:
        print("Iteration-{} for {} is at {}".format(count, name, time.ctime(time.time())))
        time.sleep(delay)
        count += 1

try:
   thread.start_new_thread( printtime, ("Thread-1", 5, 2, ) )
   thread.start_new_thread( printtime, ("Thread-2", 3, 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass