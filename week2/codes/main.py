from Dog import Dog, test_into
import sys

def my_print(msg):
    a = "1"
    # a = "2"
    # b = 2 / 0
    for i in range(1):
        print(a + msg)
    if a == "1":
        dog = Dog()
        print("over")
        dog.bark()
        test_into()

my_print("Hello")
my_print("World")




import _thread
import time

# Define a function for the thread
def print_time1( threadName, delay):
   count = 0
   while count < 5:
      # time.sleep(1)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def print_time2( threadName, delay):
   count = 0
   while count < 5:
      # time.sleep(1)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def print_time3( threadName, delay):
   count = 0
   while count < 5:
      # time.sleep(1)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# Create two threads as follows
try:
   _thread.start_new_thread( print_time1, ("Thread-1", 1, ) )
   _thread.start_new_thread( print_time2, ("Thread-2", 2, ) )
   _thread.start_new_thread(print_time3, ("Thread-3", 2,))
except:
   print ("Error: unable to start thread")

while 1:
   pass