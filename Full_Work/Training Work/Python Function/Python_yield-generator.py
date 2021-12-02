#What is Python yield?
#The yield keyword in python works like a return with the only difference is that instead of returning a value, it gives back a generator object to the caller.
#When a function is called and the thread of execution finds a yield keyword in the function, the function execution stops at that line itself and it returns a generator object back to the caller.

#Syntax : yield expression
#Description
#Python yield returns a generator object. Generators are special functions that have to be iterated to get the values.
#The yield keyword converts the expression given into a generator function that gives back a generator object. To get the values of the object, it has to be iterated to read the values given to the yield.

#Example 1
def testyield():
  yield "Welcome to Python "
output = testyield()
print(output)

#Output:<generator object testyield at 0x00000028265EB9A8>
#The output given is a generator object, which has the value we have given to yield.
#To print the message given to yield will have to iterate the generator object .

#Example 1.1
def testyield():
  yield "Welcome to Python "

output = testyield()
for i in output:
    print(i)
#Output:Welcome to Python

#What are Generators in Python?
#Generators are functions that return an iterable generator object. The values from the generator object are fetched one at a time instead of the full list together and hence to get the actual values you can use a for-loop, using next() or list() method.

#Using Generator function
def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"

test = generator()
for i in test:
    print(i)  
    

#Difference between Normal function v/s Generator function.

# Normal function
def normal_test():
    return "Hello World"
	
#Generator function
def generator_test():
	yield "Hello World"
print(normal_test()) #call to normal function
print(generator_test()) # call to generator function


#How to read the values from the generator?

#Using : list()

def even_numbers(n):
    for x in range(n):
       if (x%2==0): 
           yield x       
num = even_numbers(10)
print(list(num))


#Using : for-in
def even_numbers(n):
    for x in range(n):
       if (x%2==0): 
           yield x       
num = even_numbers(10)
for i in num:
    print(i)



#Using next()

def even_numbers(n):
    for x in range(n):
       if (x%2==0): 
           yield x       
num = even_numbers(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
#print(next(num))
#Generators are one-time Use

def even_numbers(n):
    for x in range(n):
       if (x%2==0): 
           yield x       
num = even_numbers(10)
for i in num:
    print(i)

print("\n")
print("Calling the generator again: ", list(num))



#Example: Generators and yield for Fibonacci Series

def getFibonnaciSeries(num):
    c1, c2 = 0, 1
    count = 0
    while count < num:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1
fin = getFibonnaciSeries(7)
print(fin)
for i in fin:
    print(i)
    



#Example: Calling Function with Yield

def test(n):
    return n*n

def getSquare(n):
    for i in range(n):
        yield test(i)

sq = getSquare(10)
for i in sq:
    print(i)
    

