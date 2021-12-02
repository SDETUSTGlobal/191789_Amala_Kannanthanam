#What is type() in Python?
#Python has a built-in function called type() that helps you find the class type of the variable given as input. For example, if the input is a string, you will get the output as <class ‘str’>, for the list, it will be <class ‘list’>, etc.

#Using type() command, you can pass a single argument, and the return value will be the class type of the argument given, example: type(object).
#It is also possible to pass three arguments to type(), i.e., type(name, bases, dict), in such case, it will return you a new type object.

#Syntax for type():
 #type(object)

#type(namr, bases, dict)

#Parameters: type(object)
#object: This is a mandatory parameter. If this is only parameter passed to type(), than it will return you the type of the parameter.

#Parameters: type(name, bases, dict)
#name:name of the class.
#bases: (optional). This is an optional parameter, and it is the base class
#dict: (optional). This is an optional parameter, and it is a namespace that has the definition of the class.

#Return Value:
#If the object is the only parameter passed to type() then it will return you the type of the object.
#If the params passed to type is a type(object, bases, dict), in such case, it will return a new type of object.

#Example of type()

str_list = "Welcome to Guru99"
age = 50
pi = 3.14
c_num = 3j+10
my_list = ["A", "B", "C", "D"]
my_tuple = ("A", "B", "C", "D")
my_dict = {"A":"a", "B":"b", "C":"c", "D":"d"}
my_set = {'A', 'B', 'C', 'D'}

print("The type is : ",type(str_list))
print("The type is : ",type(age))
print("The type is : ",type(pi))
print("The type is : ",type(c_num))
print("The type is : ",type(my_list))
print("The type is : ",type(my_tuple))
print("The type is : ",type(my_dict))
print("The type is : ",type(my_set))

#Example: Using type() for class object.
class test:
    s = 'testing'
t = test()
print(type(t))

#Example: Using the name, bases, and dict in type()
class MyClass:
  x = 'Hello World'
  y = 50
t1 = type('NewClass', (MyClass,), dict(x='Hello World', y=50))
print(type(t1))
print(vars(t1))

#---------------------------------------------------------------------------------------
#What is isinstance() in Python?
#Python isinstance is part of python built-in functions. Python isinstance() takes in two arguments, and it returns true if the first argument is an instance of the classinfo given as the second argument.

#Syntax isinstance() :isinstance(object, classtype)

#Parameters
#object: An object whose instance you are comparing with classtype. It will return true if the type matches otherwise false.
#class type: A type or a class or a tuple of types and/or classes.

#Return value:
#It will return true if the object is an instance of classtype and false if not.

#Examples of isinstance()
age = isinstance(51,int)
print("age is an integer:", age)

#Example : isinstance() Float check
pi = isinstance(3.14,float)
print("pi is a float:", pi)

#Example: isinstance() String check
message = isinstance("Hello World",str)
print("message is a string:", message)

#Example : isinstance() Tuple check
my_tuple = isinstance((1,2,3,4,5),tuple)
print("my_tuple is a tuple:", my_tuple)

#Example : isinstance() Set check
my_set = isinstance({1,2,3,4,5},set)
print("my_set is a set:", my_set)

#Example: isinstance() list check
my_list = isinstance([1,2,3,4,5],list)
print("my_list is a list:", my_list)

#Example: isinstance() dict check
my_dict = isinstance({"A":"a", "B":"b", "C":"c", "D":"d"},dict)
print("my_dict is a dict:", my_dict)

#Example: isinstance() test on a class

class MyClass:
    _message = "Hello World"
_class = MyClass()
print("_class is a instance of MyClass() : ", isinstance(_class,MyClass))
