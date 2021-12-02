#Python Functions Examples: Call, Indentation, Arguments & Return Values
#A Function in Python is a piece of code which runs when it is referenced. It is used to utilize the code in more than one place in a program. It is also called method or procedure.
#Python provides many inbuilt functions like print(), input(), compile(), exec(), etc. but it also gives freedom to create your own functions.
#define a function
def func1():
   print ("I am learning Python function")
   print ("still in func1")
   
func1()

def square(x):
  	return x*x
print(square(4))

def multiply(x,y=0):
	print("value of x=",x)
	print("value of y=",y)
    
	return x*y
  
	print(multiply(y=2,x=4))

#A Lambda Function in Python programming is an anonymous function or a function having no name. 
#It is a small and restricted function having no more than one line. Just like a normal function, a Lambda function can have multiple arguments with one expression.
#In Python, lambda expressions (or lambda forms) are utilized to construct anonymous functions. 
#To do so, you will use the lambda keyword (just as you use def to define normal functions). 
#Every anonymous function you define in Python will have 3 essential parts:
#1.The lambda keyword.
#2.The parameters (or bound variables), and
#3.The function body.
#A lambda function can have any number of parameters, but the function body can only contain one expression.

#example 1
adder = lambda x, y: x + y
print (adder (1, 2))

#example 2
#What a lambda returns
string='some kind of a useless lambda'
print(lambda string : print(string))

#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)

#A REGULAR FUNCTION
def pyth( funct, *args ):
	funct( *args )
def printer_one( arg ):
	return print (arg)
def printer_two( arg ):
	print(arg)
#CALL A REGULAR FUNCTION 
pyth( printer_one, 'printer 1 REGULAR CALL' )
pyth( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
pyth(lambda: printer_one('printer 1 LAMBDA CALL'))
pyth(lambda: printer_two('printer 2 LAMBDA CALL'))

#Using lambdas with Python built-ins
#IIFE in Python Lambda :IIFE stands for immediately invoked function execution
(lambda x: x + x)(2)

#lambdas in filter()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))

#lambdas in map()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))

#lambdas in reduce()
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)

###Notes to remember
#1.Lambdas, also known as anonymous functions, are small, restricted functions which do not need a name (i.e., an identifier).
#2.Every lambda function in Python has 3 essential parts: The lambda keyword,The parameters (or bound variables), and The function body.
#3.The syntax for writing a lambda is: lambda parameter: expression
#4.Lambdas can have any number of parameters, but they are not enclosed in braces
#5.A lambda can have only 1 expression in its function body, which is returned by default.
#6.At the bytecode level, there is not much difference between how lambdas and regular functions are handled by the interpreter.
#7.Lambdas support IIFE thru this syntax: (lambda parameter: expression)(argument)
#8.Lambdas are commonly used with the following python built-ins:
#9.Filter: filter (lambda parameter: expression, iterable-sequence)
#10.Map: map (lambda parameter: expression, iterable-sequences)
#11.Reduce: reduce (lambda parameter1, parameter2: expression, iterable-sequence)
#12.Do not write complicated lambda functions in a production environment because it will be difficult for code-maintainers.