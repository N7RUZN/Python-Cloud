# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os

# The create_python_script function creates a new python script
# in the current working directory, adds the line of comments to
# it declared  by the 'comments' variable, and returns the size of the new file.

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as f:
        f.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.py"))

#########################################################################

#import os

# The new_directory function creates a new directory inside the current working
# directory, then creates a new empty file inside the new directory,
# and returns the list of files in that directory.

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)

    with open(filename, 'w') as file:
        pass

    # Return the list of files in the new directory
    return os.listdir(os.getcwd())


print(new_directory("PythonPrograms", "script.py"))

#########################################################################

#import os
import datetime

# The file_date function creates a new file in the current working
# directory, checks the date that the file was modified, and returns
# just the date portion of the timestamp in the format of yyyy-mm-dd.

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    pass

  timestamp = datetime.datetime.now()
  # Convert the timestamp into a readable format, then into a string
  formatted_date = timestamp.strftime("%Y-%m-%d")
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  #return ("{year}-{month}-{day}".format(___))
  return(formatted_date)

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#########################################################################

# import os

# The parent_directory function returns the name of the directory
# that's located just above the current working directory.
# Remember that '..' is a relative path alias that means "go up to the parent directory".

def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    cwd = os.getcwd()
    # relative_parent = os.path.join(, cwd)
    # print(os.pardir)

    abspath = os.path.abspath(os.path.join(cwd, os.pardir))

    # print(relative_parent)
    # Return the absolute path of the parent directory
    # print(os.path.abspath(relative_parent))
    return abspath


print(parent_directory())