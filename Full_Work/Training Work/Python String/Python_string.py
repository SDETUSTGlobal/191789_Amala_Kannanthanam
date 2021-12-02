#accessing values in string
var1 = "Python!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])

#replace
oldstring = 'I like Python' 
newstring = oldstring.replace('like', 'love')
print(newstring)

#uppercase lowercase
string="python at Python"
print(string.upper())
# capitalize
string="python at Python"		
print(string.capitalize())

#lower
string="PYTHON AT Python"
print(string.lower())

#“join” function
print(":".join("Python"))

#Reversing string
string="12345"		
print(''.join(reversed(string)))

#Split Strings
word="Python career Python"		
print(word.split(' '))

#strip-----------------------------

#strip() Method in Python
str1 = "Welcome to Python!"
after_strip = str1.strip()

#strip() on Invalid Data Type
mylist = ["a", "b", "c", "d"]
print(mylist.strip())

#strip() Without character parameter

str1 = "Welcome to Python!"
after_strip = str1.strip()
print(after_strip)
str2 = "Welcome to Python!"
after_strip1 = str2.strip()
print(after_strip1)

#strip() Passing character parameters
str1 = "****Welcome to Python!****"
after_strip = str1.strip("*")
print(after_strip)
str2 = "Welcome to Python99!"
after_strip1 = str2.strip("99!")
print(after_strip1)
str3 = "Welcome to Python!"
after_strip3 = str3.strip("to")
print(after_strip3)

##reasons for using Python strip function
#It helps to remove the characters at the start of the string and also at the end of the string based on the characters given to be removed from the original string.
#If the characters given do not match the original string, the string will be returned as it is.
#If the characters to be removed are not specified, then the whitespaces from the start and end of the original string will be removed.
#If there is no white space at the start or end than the string will be returned as it is.



