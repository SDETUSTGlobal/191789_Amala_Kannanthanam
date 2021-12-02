#What is Python Enumerate?
#Python Enumerate() is a buit-in function available with the Python library. It takes the given input as a collection or tuples and returns it as an enumerate object.
 #The Python Enumerate() command adds a counter to each item of the iterable object and returns an enumerate object as an output string.
 
#Syntax of Python enumerate() : enumerate(iterable, startIndex)

#Parameters
#Three parameters are:
#Iterable: an object that can be looped.
#StartIndex: (optional) The count will start with the value given in the startIndex for the first item in the loop and
# increment it for the nextitem till it reaches the end of the loop.
 
#Enumerate() in Python Example

mylist = ['A', 'B' ,'C', 'D']
e_list = enumerate(mylist)
print(list(e_list))

#UsingEnumerate() on a list with startIndex
mylist = ['A', 'B' ,'C', 'D']
e_list = enumerate(mylist,2)
print(list(e_list))

#Looping Over an Enumerate object
mylist = ['A', 'B' ,'C', 'D']
for i in enumerate(mylist):
  print(i)
  print("\n")
print("Using startIndex as 10")    
for i in enumerate(mylist, 10):
  print(i)
  print("\n")
  
#Enumerating a Tuple
my_tuple = ("A", "B", "C", "D", "E")
for i in enumerate(my_tuple):
  print(i)
  
#Enumerating a String
my_str = "Guru99 "
for i in enumerate(my_str):
  print(i)
  
#Enumerate a dictionary
my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}
for i in enumerate(my_dict):
  print(i)

#Advantages of using Enumerate
#Enumerate allows you to loop through a list, tuple, dictionary, string, and gives the values along with the index.
#To get index value using for-loop, you can make use of list.index(n). However, list.index(n) is very expensive as it will traverse the for-loop twice. Enumerate is very helpful in such a case as it gives the index and items at one go.