#What is Python Sleep?
#Python sleep() is a function used to delay the execution of code for the number of seconds given as input to sleep(). The sleep() command is a part of the time module. You can use the sleep() function to temporarily halt the execution of your code. For example, you are waiting for a process to complete or a file upload.

#time.sleep() Syntax:
#import time
#time.sleep(seconds)

#Parameters:
#seconds: The number of seconds you want the execution of your code to be halted.

#Example: Using sleep() function in Python

#Follow the steps given below to add sleep() in your python script.
#Step 1:
#import time
#Step 2: Add time.sleep()
#The number 5 given as input to sleep(), is the number of seconds you want the code execution to halt when it is executed.
#time.sleep(5)

#Example
import time
print("Welcome to Python")
time.sleep(5)
print("This message will be printed after a wait of 5 seconds")

#How to delay the execution of function using sleep()?

#Example:
import time
print('Code Execution Started')
def display():
    print('Welcome to Python')
    time.sleep(5)
display()
print('Function Execution Delayed')

#What are the different ways to add a delay in Python Script?
#Using sleep() function

#Example:
#The code has a for loop that will take the string variable and print each character with a delay of 1 seconds.

import time
my_message = "Python"
for i in my_message:
   print(i)
   time.sleep(1)

#Using asyncio.sleep function available from (Python 3.4 or higher)

#Example:
import asyncio
print('Code Execution Started')
async def display():
    await asyncio.sleep(5)
    print('Welcome to Python')
asyncio.run(display())

#Using Event().wait
#The Event().wait method comes from the threading module. Event.wait() method will halt the execution of any process for the number of seconds it takes as an argument.

#Example:

#The code is using Event().wait(5).The number 5 is the number of seconds the code will delay to go to the next line that calls the function display(). Once the 5 seconds are done, the function display() will be called, and the message will be printed inside in the terminal.

from threading import Event
print('Code Execution Started')
def display():
    print('Welcome to Python')
Event().wait(5) 
display()


#Using Timer

#Example:

from threading import Timer
print('Code Execution Started')
def display():
    print('Welcome to Python')
t = Timer(5, display)  
t.start()