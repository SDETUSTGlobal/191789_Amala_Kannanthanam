#What is Python Range?
#Python range() is a built-in function available with Python from Python(3.x), and it gives a sequence of numbers based on the start and stop index given. In case the start index is not given, the index is considered as 0, and it will increment the value by 1 till the stop index.
#For example range(5) will output you values 0,1,2,3,4 .The Python range()is a very useful command and mostly used when you have to iterate using for loop.

#Syntax : range(start, stop, step)
#Parameters
#start: (optional) The start index is an integer, and if not given, the default value is 0.
#stop: The stop index decides the value at which the range function has to stop. It is a mandatory input to range function. The last value will be always 1 less than the stop value.
#step: (optional).The step value is the number by which the next number is range has to be incremented, by default, it is 1.
#Return value:
#The return value is a sequence of numbers from the given start to stop index.

#Using range()
for i in range(10):
    print(i, end =" ")


#Using start and stop in range()
for i in range(3, 10):
    print(i, end =" ")    
 

#Using start, stop and step
for i in range(3, 10, 2):
    print(i, end =" ")
    

#Incrementing the values in range using a positive step.
for i in range(1, 30, 5):
    print(i, end =" ")
    

#Reverse Range: Decrementing the values using negative step.
for i in range(15, 5, -1):
    print(i, end =" ")
    

#Using floating numbers in Python range()
for i in range(10):
    print(i, end =" ")
    

#Using for-loop with Python range()
arr_list = ['Mysql', 'Mongodb', 'PostgreSQL', 'Firebase']

for i in range(len(arr_list)):
    print(arr_list[i], end =" ")
    

#Using Python range() as a list
print(list(range(10)))


#U#sing characters in python range()
for c in range ('z'):
        print(c, end =" ")
        
        #Check for output -
def get_alphabets(startletter, stopletter, step):
    for c in range(ord(startletter.lower()), ord(stopletter.lower()), step):
        yield chr(c)

print(list(get_alphabets("a", "h", 1)))

#How to Access Range Elements Using for-loop
for i in range(6):
    print(i)
    

#Using index
startvalue = range(5)[0] 
print("The first element in range is = ", startvalue) 

secondvalue = range(5)[1] 
print("The second element in range is = ", secondvalue) 

lastvalue = range(5)[-1]
print("The first element in range is = ", lastvalue)


#Using list()
print(list(range(10)))

#Example: Get even numbers using range()
for i in range(2, 20, 2):
    print(i, end =" ")
    

#Merging two-range() outputs
from itertools import chain 

print("Merging two range into one") 
frange =chain(range(10), range(10, 20, 1))
for i in frange: 
    print(i, end=" ")

#Using range() With NumPy
#The NumPy module has arange() function that works and gives similar output like range(). The arrange() takes in the same parameters like range().

#Syntax:arange(start, stop, step)

#To work with NumPy follow the steps given below.
#Step 1: Import NumPy module

#import numpy

#Incase while execution, it gives an error saying numpy module not found, you need to install the module as shown in step 2.

#Step 2: Install NumPy

#pip install numpy

#Step 3: Working Example of arange() using NumPy

import numpy as np 

for  i in np.arange(10):
   print(i, end =" ")        


#Floating point numbers using NumPy arange()
import numpy as np 

for  i in np.arange(0.5, 1.5, 0.2):
   print(i, end =" ")    
   

