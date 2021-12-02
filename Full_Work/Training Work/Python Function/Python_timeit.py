#What is Python Timeit()?
#Python timeit() is a method in Python library to measure the execution time taken by the given code snippet. The Python library runs the code statement 1 million times and provides the minimum time taken from the given set of code snippets. Python timeit() is a useful method that helps in checking the performance of the code.

#Syntax: timeit.timeit(stmt, setup,timer, number)

#Parameters
#stmt: This will take the code for which you want to measure the execution time. The default value is “pass”.
#setup: This will have setup details that need to be executed before stmt. The default value is “pass.”
#timer: This will have the timer value, timeit() already has a default value set, and we can ignore it.
#number: The stmt will execute as per the number is given here. The default value is 1000000.

#To work with timeit(), we need to import the module, as shown below:
import timeit

#Code Example 1:
# testing timeit()
import timeit
print(timeit.timeit('output = 10*5'))

#Timing Multiple lines in python code

#Example 1: Using semicolon
import timeit
print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a+b'))

#Example 2: Using triple quotes
import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module))



#timeit – Methods:
#Here, are 2 important timeit methods

#timeit.default_timer() : This will return the default time when executed.
#timeit.repeat(stmt, setup, timer, repeat, number) : same as timeit() , but with repeat the timeit() is called the number of times repeat is given.

#Program Example 1:
# testing timeit()
import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.timeit(stmt=testcode, setup=import_module))

#Example 2:
#default_timer() Example

# testing timeit()
 
import timeit
import random
 
def test(): 
    return random.randint(10, 100)
 
starttime = timeit.default_timer()
print("The start time is :",starttime)
test()
print("The time difference is :", timeit.default_timer() - starttime)

#Example 3: timeit.repeat()
# testing timeit()
import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))


