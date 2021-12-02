#syntax for PythonString Count()
#Python count function syntax:string.count(char or substring, start, end)

#Parameters of Python Syntax
#Char or substring: You can specify a single character or substring you are wants to search in the given string. It will return you the count of the character or substring in the given string.
#start : (optional) It indicates the start index from where the search will begin. If not given, it will start from 0. For example, you want to search for a character from the middle of the string. You can give the start value to your count function.
#end: (optional) It indicates the end index where the search ends. If not given, it will search till the end of the list or string given. For example, you don’t want to scan the entire string and limit the search till a specific point you can give the value to end in your count function, and the count will take care of searching till that point.
#ReturnValue
#The count() method will return an integer value, i.e., the count of the given element from the given string. It returns a 0 if the value is not found in the given string.

#Count Method on a String
str1 = "Hello World"
str_count1 = str1.count('o')  # counting the character “o” in the givenstring
print("The count of 'o' is", str_count1)
str_count2 = str1.count('o', 0,5)
print("The count of 'o' usingstart/end is", str_count2)

#Count occurrence of a character in a given string
str1 = "Welcome to Python "
str_count1 = str1.count('u')  # counting the character “u” in the given string
print("The count of 'u' is", str_count1)
str_count2 = str1.count('u', 6,15)
print("The count of 'u' usingstart/end is", str_count2)

#Count occurrence of substring in a given string
str1 = "Welcome to Python "
str_count1 = str1.count('to') # counting the substring “to” in the givenstring
print("The count of 'to' is", str_count1)
str_count2 = str1.count('to', 6,15)
print("The count of 'to' usingstart/end is", str_count2)
