#What is Python Counter?
#Python Counter is a container that will hold the count of each of the elements present in the container. The counter is a sub-class available inside the dictionary class.

#The counter is a sub-class available inside the dictionary class. Using the Python Counter tool, you can count the key-value pairs in an object, also called a hash table object.


#Why use Python Counter?
#Here, are major reasons for using Python 3 Counter:

#The Counter holds the data in an unordered collection, just like hashtable objects. The elements here represent the keys and the count as values.
#It allows you to count the items in an iterable list.
#Arithmetic operations like addition, subtraction, intersection, and union can be easily performed on a Counter.
#A Counter can also count elements from another counter.

#Syntax: Counter(list)

#example 1
from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))
#---------------------------------------------------------
#Counter with String

from collections import Counter
my_str = "Welcome to Guru99 Tutorials!"
print(Counter(my_str))

#------------------------------------------------------
#Counter with List

from collections import Counter
list1 = ['x','y','z','x','x','x','y','z']
print(Counter(list1))

#----------------------------------------------------------------
#Counter with Dictionary

from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))

#--------------------------------------------------------------------
#Counter with Tuple

from collections import Counter
tuple1 = ('x','y','z','x','x','x','y','z')
print(Counter(tuple1))

#--------------------------------------------------------------------------
#Accessing, Initializing and Updating Counters

#Initializing Counter
from collections import Counter
print(Counter("Welcome to Python"))   #using string
print(Counter(['x','y','z','x','x','x','y', 'z'])) #using list
print(Counter({'x': 4, 'y': 2, 'z': 2})) #using dictionary
print(Counter(('x','y','z','x','x','x','y', 'z'))) #using tuple

#Initialize a empty Counter
from collections import Counter
_count = Counter()

#Updating Counter
_count.update('Welcome to Python')

#example :
from collections import Counter
_count = Counter()
_count.update('Welcome to Python')
print(_count)

#-------------------------------------------------------------------
#Accessing Counter

from collections import Counter
_count = Counter()
_count.update('Welcome to Guru99 Tutorials!')
print('%s : %d' % ('u', _count['u']))
print('\n')
for char in 'Guru':
    print('%s : %d' % (char, _count[char]))
    
#-----------------------------------------------------------------------------
#Deleting an Element from Counter

from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2}
del dict1["x"]
print(Counter(dict1))

#----------------------------------------------------------------------------------
#Arithmetic operation on Python Counter

from collections import Counter
counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})
counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })
#Addition
counter3 = counter1 + counter2 # only the values that are positive will be returned.
print(counter3)
#Subtraction
counter4 = counter1 - counter2 # all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output
print(counter4)
#Intersection
counter5 = counter1 & counter2 # it will give all common positive minimum values from counter1 and counter2
print(counter5)
#Union
counter6 = counter1 | counter2 # it will give positive max values from counter1 and counter2
print(counter6)

#----------------------------------------------------------------------------------------

#Methods Available on Python Counter
#There are some important methods available with Counter, here is the list of same:

#elements() : This method will return you all the elements with count >0. Elements with 0 or -1 count will not be returned.
#most_common(value): This method will return you the most common elements from Counter list.
#subtract(): This method is used to deduct the elements from another Counter.
#update(): This method is used to update the elements from another Counter.

#--------------------------------------------------------------------------------------------

#Example : elements()
from collections import Counter
counter1 =  Counter({'x': 5, 'y': 2, 'z': -2, 'x1':0})

_elements = counter1.elements() # will give you all elements with positive value and count>0
for a in _elements:
    print(a)
    
#-----------------------------------------------------------------------------------------------------------
#Example: most_common(value)
from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
common_element = counter1.most_common(2) # The dictionary will be sorted as per the most common element first followed by next.
print(common_element)
common_element1 = counter1.most_common() # if the value is not given to most_common , it will sort the dictionary and give the most common elements from the start.The last element will be the least common element.
print(common_element1)

#------------------------------------------------------------------------------------------------------------
#Example:subtract()
from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
counter2 = Counter({'x': 2, 'y':5})
counter1.subtract(counter2)
print(counter1)

#----------------------------------------------------------------------------------------------------------------

#Example:update()
from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
counter2 = Counter({'x': 2, 'y':5})
counter1.update(counter2)
print(counter1)
#-------------------------------------------------------------------------------------------------------------
#Reassigning Counts in Python
#You can re-assign counts of Counter as shown below:

#dictionary : {‘x’: 5, ‘y’: 12, ‘z’: -2, ‘x1’:0}

#You can change the count of the element as shown below:

from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
counter1['y'] = 20
print(counter1)

#-------------------------------------------------------------------------------------------
#Get and set the count of Elements using Counter
#To get the count of an element using Counter you can do as follows:

from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
print(counter1['y']) # this will give you the count of element 'y'


#To set the count of the element you can do as follows:

from collections import Counter
counter1 =  Counter({'x': 5, 'y': 12, 'z': -2, 'x1':0})
print(counter1['y'])
counter1['y'] = 20
counter1['y1'] = 10
print(counter1)
