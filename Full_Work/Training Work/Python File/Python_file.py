#How to Open a Text File in Python
#To open a file, you need to use the built-in open function. The Python file open function returns a file object that contains methods and attributes to perform various operations for opening files in Python.

#Syntax of Python open file function

#file_object  = open("filename", "mode")
#filename: gives name of the file that the file object has opened.
#mode: attribute of a file object tells you which mode a file was opened in.


#How to Create a Text File in Python
#With Write to file Python, you can create a .text files (Python.txt) by using the code, we have demonstrated here:

#Step 1) Open the .txt file

#f= open("Python.txt","w+")
#We declared the variable f to open a file named Python.txt. Open takes 2 arguments, the file that we want to open and a string that represents the kinds of permission or operation we want to do on the file
#Here, we used “w” letter in our argument, which indicates Python write to file and it will create file in Python if it does not exist in library
#Plus sign indicates both read and write for Python create file operation.

#Step 2) Enter data into the file

#for i in range(10):
 #    f.write("This is line %d\r\n" % (i+1))
     
#We have a for loop that runs over a range of 10 numbers.
#Using the write function to enter data into the file.
#The output we want to iterate in the file is “this is line number”, which we declare with Python write file function and then percent d (displays integer)
#So basically we are putting in the line number that we are writing, then putting it in a carriage return and a new line character.

#Step 3) Close the file instance
#f.close()
#This will close the instance of the file Python.txt stored


#How to Append to a File in Python
#You can also append/add a new text to the already existing file or a new file.

#Step 1)

#f=open("Python.txt", "a+")
#Once again if you could see a plus sign in the code, it indicates that it will create a new file if it does not exist. But in our case we already have the file, so we are not required to create a new file for Python append to file operation.

#Step 2)

#for i in range(2):
 #    f.write("Appended line %d\r\n" % (i+1))
#This will write data into the file in append mode.

#How to Read Files in Python
#You can read a file in Python by calling .txt file in a “read mode”(r).

#Step 1) Open the file in Read mode

#f=open("Python.txt", "r")

#Step 2) We use the mode function in the code to check that the file is in open mode. If yes, we proceed ahead

#if f.mode == 'r':

#Step 3) Use f.read to read file data and store it in variable content for reading files in Python

#contents =f.read()
#Step 4) Print contents for Python read text file

#File Modes in Python
#Following are the various File Modes in Python:

#Mode	Description
#‘r’	This is the default mode. It Opens file for reading.
#‘w’	This Mode Opens file for writing.If file does not exist, it creates a new file.If file exists it truncates the file.
#‘x’	Creates a new file. If file already exists, the operation fails.
#‘a’	Open file in append mode.
#If file does not exist, it creates a new file.
#‘t’	This is the default mode. It opens in text mode.
#‘b’	This opens in binary mode.
#‘+’	This will open a file for reading and writing (updating)

#Python 3 Example

#Below is another Python print() to File Example:

def main():
    f= open("Python.txt","w+")
    #f=open("Python.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    #f=open("Python.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)
if __name__== "__main__":
  main()