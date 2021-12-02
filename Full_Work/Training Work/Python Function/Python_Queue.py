#What is Python Queue?
#A queue is a container that holds data. The data that is entered first will be removed first, and hence a queue is also called “First in First Out” (FIFO). The queue has two ends front and rear. The items are entered from the rear and removed from the front side.

#Types of Queue in Python
#There are mainly two types of queue in Python:

#First in First out Queue: For this, the element that goes first will be the first to come out.
#To work with FIFO, you have to call Queue() class from queue module.

#Last in First out Queue: Over here, the element that is entered last will be the first to come out.
#To work with LIFO, you have to call LifoQueue() class from the queue module.

#Python queue Installation
#Step 1) You just have to import the queue module, as shown below:
#import queue
#The module is available by default with python, and you don’t need any additional installation to start working with the queue. There are 2 types of queue FIFO (first in first out) and LIFO (last in first out).

#Step 2) To work with FIFO queue , call the Queue class using the queue module imported as shown below:
#import queue
#q1 = queue.Queue()

#Step 3) To work with LIFO queue call the LifoQueue() class as shown below:
#import queue
#q1 = queue.LifoQueue()

#Methods available inside Queue and LifoQueue class

#put(item): This will put the item inside the queue.
#get(): This will return you an item from the queue.
#empty(): It will return true if the queue is empty and false if items are present.
#qsize(): returns the size of the queue.
#full(): returns true if the queue is full, otherwise false.

#First In First Out Queue Example
#In the case of first in first out, the element that goes first will be the first to come out.
#----------------------------------------------------------------------------------------------------
#Add and item in a queue

import queue
q1 = queue.Queue()
q1.put(10) #this will additem 10 to the queue.



#By default, the size of the queue is infinite and you can add any number of items to it. In case you want to define the size of the queue the same can be done as follows


import queue
q1 = queue.Queue(5) #The max size is 5.
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full()) # will return true.
#-----------------------------------------------------------------------------------------------------
#Remove an item from the queue

import queue
q1 = queue.Queue()
q1.put(10)
item1 = q1.get()
print('The item removed from the queue is ', item1)

#-----------------------------------------------------------------------------------------------------------------------------

#To work with LIFO, i.e., last in the first out queue, we need to import the queue module and make use of the LifoQueue() method.

#-------------------------------------------------------------------------------------------
#Add and item in a queue

import queue
q1 = queue.LifoQueue()
q1.put(10)

#-------------------------------------------------------------------------------------------
#Remove an item from the queue
#To remove an item from the LIFOqueue you can make use of get() method .

import queue
q1 = queue.LifoQueue()
q1.put(10)
item1 = q1.get()
print('The item removed from the LIFO queue is ', item1)

#----------------------------------------------------------------------------------------------------------
#Add and item in a FIFOqueue
import queue
q1 = queue.Queue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
#-------------------------------------------------------------------------------------------------------------
#Remove an item from the FIFOqueue
import queue
q1 = queue.Queue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

#------------------------------------------------------------------------------------------
#Add and item in a LIFOqueue
import queue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

#----------------------------------------------------------------------------------------------------
#Remove an item from the LIFOqueue
import queue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

#-------------------------------------------------------------------------------------------------------------------------
#Sorting Queue
#Following example shows the queue sorting.The algorithm used for sorting is bubble sort.

import queue
q1 = queue.Queue()
#Addingitems to the queue
q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
q1.put(10)
#using bubble sort on the queue
n =  q1.qsize()
for i in range(n):
    x = q1.get() # the element is removed
    for j in range(n-1):
        y = q1.get() # the element is removed
        if x > y :  
            q1.put(y)   #the smaller one is put at the start of the queue
        else:
            q1.put(x)  # the smaller one is put at the start of the queue
            x = y     # the greater one is replaced with x and compared again with nextelement
    q1.put(x)

while (q1.empty() == False): 
    print(q1.queue[0], end = " ")
    q1.get()

#----------------------------------------------------------------------------------------------------------
#The following example shows how to get the queue reversed.

#Example:
import queue
q1 = queue.Queue()

q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
q1.put(10)

def reverseQueue (q1src, q2dest) :  
    buffer = q1src.get()
    if (q1src.empty() == False) :
        reverseQueue(q1src, q2dest)      #using recursion
    q2dest.put(buffer)
    return q2dest

q2dest = queue.Queue()
qReversed = reverseQueue(q1,q2dest)

while (qReversed.empty() == False): 
    print(qReversed.queue[0], end = " ")
    qReversed.get()