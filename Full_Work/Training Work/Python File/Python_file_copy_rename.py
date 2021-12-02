#Python Copy File Methods
#Python provides in-built functions for easily copying files using the Operating System Shell utilities.

#Command to Copy File :shutil.copy(src,dst)
#Command to Copy File with MetaData Information:shutil.copystat(src,dst)

#How to Copy a File in Python
#Here are the steps to copy file in Python using the shutil copy() method:

#Step 1) Capture the original path in the current directory
#Before, we copy a file, we need to get the the path to the original file in the current directory. In the code –
#First we are going to check that our “Python.txt” file exists or not. Since we have created Python.txt file earlier, we know it exists, and we will carry on further with the code
#We store the file path in the variable “src” if your file exist
#Once we get the path, we going to separate the path and the file name
#For that, we are going to use the split path.split function on source variable
#Code when executed prints out “file name” and “file path” separately

#Step 2) Create a copy of our existing file using shutil module
#We use Shutil Module to create a copy of the existing file. Here we used to create a copy of our existing file “Python.txt.”
#Take the original file name “Python.txt” and add letters .bak at the end “Python.txt.bak”. This name with .bak extension is going to be our duplicate copy
#And then we going to use utility’s copy function to copy from source to the destination
#When you run the code, you will see a duplicate file with .bak extension is created on right-hand side of the panel

#Step 3) Copy meta-data associated with the file, file permission and other information
#Copy function only copies the content of the file but no other information. To copy meta-data associated with the file, file permission and other information you have to use “copystat” function. Before we run this code, we have to delete our copy file “Python.text.bak”.
#Once you deleted the file and run the program it will create a copy of your .txt file but this time with all the information like file permission, modification time and meta-data information. You can go to your O.S shell to verify the information.

import os
import shutil
from os import path
 Python main():
    # make a duplicate of an existing file
    if path.exists("Python.txt"):
    # get the path to the file in the current directory
        src = path.realpath("Python.txt");
    
	#seperate the path from the filter
	head, tail = path.split(src)
	print("path:" +head)
	print("file:" +tail)
	
	#let's make a backup copy by appending "bak" to the name
	dst = src+".bak"
	# nowuse the shell to make a copy of the file
	shutil.copy(src, dst)
	
	#copy over the permissions,modification
	shutil.copystat(src,dst)
	
if __name__=="__main__":
	main()
    
#Step 4) Fetch the information
#You can fetch the information about the text file last modified


# Example file for working with o.s path module
from os import path
import datetime
import time
Python main():
    # Get the modification time
    t = time.ctime(path.getmtime("Python.txt.bak"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("Python.txt.bak")))
if __name__ == "__main__":
    main()
    
  
#Code Line#68- It tells the day, date, month, year and time when .txt file (Python) was last modified. We use the path module to get the file modification time details, and then we are going to use the time classes c time function to convert that into a readable time. So when we run the code, we can see the file Python.txt was last modified on Mon, Jan 8th at 13:35 2018.
#Code Line#70- It does the same thing giving information about file modification, but it has a different format to represent it. Here we use Get Modification Time function (path.getmtime(“Python.txt”)). Now instead of using the c time function we going to use From Time Stamp function and going to construct a date time object. In output, you can see file modification time detail is printed out in different format 2018-01-08, 13:35:51.334072

-----------------------------------------------------------------------------------------------------------------------------------------
#Python Rename File
#Python rename() file is a method used to rename a file or a directory in Python programming. The Python rename() file method can be declared by passing two arguments named src (Source) and dst (Destination).

#Syntax:os.rename(src, dst)

#Parameters
#src: Source is the name of the file or directory. It should must already exist.
#dst: Destination is the new name of the file or directory you want to change.

#Example:
import os
from os import path
Python main():
	# make a duplicate of an existing file
    if path.exists("Python.txt"):
	# get the path to the file in the current directory
        src = path.realpath("Python.txt");
		
	# rename the original file
        os.rename('Python.txt','career.Python.txt') 
		
if __name__ == "__main__":
    main()