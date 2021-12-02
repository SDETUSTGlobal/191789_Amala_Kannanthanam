#Python allows you to quickly create zip/tar archives.

#Following command will zip entire directory :shutil.make_archive(output_filename, 'zip', dir_name)
#Following command gives you control on the files you want to archive :ZipFile.write(filename)

#steps to create Zip File in Python

#Step 1) To create an archive file from Python, make sure you have your import statement correct and in order. Here the import statement for the archive is from shutil import make_archive

#Import make_archive class from module shutil

#Use the split function to split out the directory and the file name from the path to the location of the text file (Python)
#Then we call the module “shutil.make_archive(“Python archive, “zip”, root_dir)” to create archive file, which will be in zip format
#After then we pass in the root directory of things we want to be zipped up. So everything in the directory will be zipped
#When you run the code, you can see the archive zip file is created on the right side of the panel.

#Step 2) Once your archive file is made, you can right-click on the file and select the O.S, and it will show your archive files in it as shown below
#Now your archive.zip file will appear on your O.S (Windows Explorer)

#Step 3) When you double-click on the file, you will see the list all the files in there.

#Step 4) In Python we can have more control over archive since we can define which specific file to include under archive. In our case, we will include two files under archive “Python.txt” and “Python.txt.bak”.

#Step 5) When you -> right click on file (testPython.zip) and -> select your O.S (Windows Explorer), it will show the archive files in the folder as shown below.
#When you double click on file “testPython.zip”, it will open another window, and this will show the files included in it.

#example 1
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
    # Check if file exists
    if path.exists("Python.txt"):
#get the path to the file in the current directory
	src = path.realpath("Python.txt");
# rename the original file
	os.rename("career.Python.txt","Python.txt")
# now put things into a ZIP archive
	root_dir,tail = path.split(src)
    shutil.make_archive("Python archive", "zip", root_dir)
# more fine-grained control over ZIP files
	with ZipFile("testPython.zip","w") as newzip:
	newzip.write("Python.txt")
	    newzip.write("Python.txt.bak")
if __name__== "__main__":
	  main()

#Example2

import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

    # Check if file exists
     if path.exists("Python.txt"):
    # get the path to the file in the current directory
        src = path.realpath("Python.txt");
    # rename the original file
        os.rename("career.Python.txt","Python.txt")
    # now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("Python archive","zip",root_dir)
    # more fine-grained control over ZIP files
        with ZipFile("testPython.zip", "w") as newzip:
            newzip.write("Python.txt")
            newzip.write("Python.txt.bak")
            
#Code Explanation

#Import Zipfile class from zip file Python module. This module gives full control over creating zip files
#We create a new Zipfile with name ( “testPython.zip, “w”)
#Creating a new Zipfile class, requires to pass in permission because it’s a file, so you need to write information into the file as newzip
#We used variable “newzip” to refer to the zip file we created
#Using the write function on the “newzip” variable, we add the files “Python.txt” and “Python.txt.bak” to the archive