#Syntax of format() function in Python templatestring.format(val1, val2...)
#Parameters:val1, val2 … : The values that need to replace in the given template string that has placeholders in the form of curly brackets {}. The placeholders can be a string, key/value pair, integers, floating-point numbers, characters, etc.
#Return value:It will return the final string, with valid values replaced in place of the placeholders given in curly brackets.
#Placeholders:The placeholders in the template string are represented using curly brackets, e.g. {}. The placeholder can be empty {}, or it can have a variable for e.g {name} , or it can have a number index e.g {0} , {1} etc.

#Empty Placeholder replaced with a string value
print ("Welcome to {} tutorials".format("Python"))
#Empty Placeholder replaced with a numeric value
print ("Welcome to Python{} Tutorials".format("!"))
#Using variable or keyword arguments inside the Placeholder
print ("Welcome to {name}{num} Tutorials".format(name="Python", num="!"))
#Using index or positional arguments inside the Placeholder
print ("Welcome to {0}{1} Tutorials".format("Python","!"))
#Using multiple placeholders inside a string
print ("{} is {} new kind of {} experience!".format("Python", "totally","learning"))


#Using class with format()
class MyClass:
    msg1="Python"
    msg2="Tutorials"   
print("Welcome to {c.msg1}! {c.msg2}!".format(c=MyClass()))

#Using dictionary with format()
my_dict = {'msg1': "Welcome", 'msg2': 'Python'}
print("{m[msg1]} to {m[msg2]} Tutorials!".format(m=my_dict))

#Padding Variable Substitutions
print("I have {:5} dogs and {:5} cat".format(2,1))
