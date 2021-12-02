#Python exists()
#Python exists() method is used to check whether specific file or directory exists or not. It is also used to check if a path refers to any open file descriptor or not. It returns boolean value true if file exists and returns false otherwise. It is used with os module and os.path sub module as os.path.exists(path).

#How to Check If a File Exists in Python using os.path.exists()
import os.path
from os import path
def main():

   print ("File exists:"+str(path.exists('Python.txt')))
   print ("File exists:" + str(path.exists('career.Python.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()
   
#Python isfile()
#The Python isfile() method is used to find whether a given path is an existing regular file or not. It returns a boolean value true if the specific path is an existing file or else it returns false. It can be used by the syntax : os.path.isfile(path).

#os.path.isfile()
import os.path
from os import path
def main():

	print ("Is it File?" + str(path.isfile('Python.txt')))
	print ("Is it File?" + str(path.isfile('myDirectory')))
if __name__== "__main__":
	main()
    
#os.path.isdir()
import os.path
from os import path

def main():

   print ("Is it Directory?" + str(path.isdir('Python.txt')))
   print ("Is it Directory?" + str(path.isdir('myDirectory')))

if __name__== "__main__":
   main()
   
#pathlibPath.exists() For Python 3.4
import pathlib
file = pathlib.Path("Python.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")

