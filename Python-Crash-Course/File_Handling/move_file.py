# Use the shutil.move() function
# Use the shutil.move() function
# shutil.move(source, destination, copy_function = copy2)

import shutil

# absolute path
src_path = r"E:\pynative\reports\sales.txt"
dst_path = r"E:\pynative\account\sales.txt"
shutil.move(src_path, dst_path)

# Move File and Rename

import os
import shutil

src_folder = r"E:\pynative\reports\\"
dst_folder = r"E:\pynative\account\\"
file_name = 'sales.csv'

# check if file exist in destination
if os.path.exists(dst_folder + file_name):
    # Split name and extension
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]
    # Adding the new name
    new_base = only_name + '_new' + extension
    # construct full file path
    new_name = os.path.join(dst_folder, new_base)
    # move file
    shutil.move(src_folder + file_name, new_name)
else:
    shutil.move(src_folder + file_name, dst_folder + file_name)

    # Move Multiple Files
import shutil

source_folder = r"E:\pynative\reports\\"
destination_folder = r"E:\pynative\account\\"
files_to_move = ['profit.csv', 'revenue.csv']

# iterate files
for file in files_to_move:
    # construct full file path
    source = source_folder + file
    destination = destination_folder + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)
Output:

Moved: profit.csv
Moved: revenue.csv
Home » Python » File Handling » Move Files Or Directories in Python
Move Files Or Directories in Python
Updated on: January 19, 2022 | 3 Comments

In this Python tutorial, you’ll learn how to move files and folders from one location to another.

After reading this article, you’ll learn: –

How to move single and multiple files using the shutil.move() method
Move files that match a pattern (wildcard)
Move an entire directory
Steps to Move a File in Python
Python shutil module offers several functions to perform high-level operations on files and collections of files. We can move files using the shutil.move() method. The below steps show how to move a file from one directory to another.

Find the path of a file
We can move a file using both relative path and absolute path. The path is the location of the file on the disk.
An absolute path contains the complete directory list required to locate the file. For example, /home/Pynative/sales.txt is an absolute path to discover the sales.txt.

Use the shutil.move() function
The shutil.move() function is used to move a file from one directory to another.
First, import the shutil module and Pass a source file path and destination directory path to the move(src, dst) function.

Use the os.listdir() and shutil move() function to move all files
Suppose you want to move all/multiple files from one directory to another, then use the os.listdir() function to list all files of a source folder, then iterate a list using a for loop and move each file using the move() function.

Example: Move a Single File
Use the shutil.move() method move a file permanently from one folder to another.

shutil.move(source, destination, copy_function = copy2)
source: The path of the source file which needs to be moved.
destination: The path of the destination directory.
copy_function: Moving a file is nothing but copying a file to a new location and deletes the same file from the source. This parameter is the function used for copying a file and its default value is shutil.copy2(). This could be any other function like copy() or copyfile().
In this example, we are moving the sales.txt file from the report folder to the account folder.

import shutil

# absolute path
src_path = r"E:\pynative\reports\sales.txt"
dst_path = r"E:\pynative\account\sales.txt"
shutil.move(src_path, dst_path)
Note:

The move() function returns the path of the file you have moved.
If your destination path matches another file, the existing file will be overwritten.
It will create a new directory if a specified destination path doesn’t exist while moving file.
Move File and Rename
Let’s assume your want to move a file, but the same file name already exists in the destination path. In such cases, you can transfer the file by renaming it.

Let’s see how to move a file and change its name.

Store source and destination directory path into two separate variables
Store file name into another variable
Check if the file exists in the destination folder
If yes, Construct a new name for a file and then pass that name to the shutil.move() method.
Suppose we want to move sales.csv into a folder called to account, and if it exists, rename it to sales_new.csv and move it.

import os
import shutil

src_folder = r"E:\pynative\reports\\"
dst_folder = r"E:\pynative\account\\"
file_name = 'sales.csv'

# check if file exist in destination
if os.path.exists(dst_folder + file_name):
    # Split name and extension
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]
    # Adding the new name
    new_base = only_name + '_new' + extension
    # construct full file path
    new_name = os.path.join(dst_folder, new_base)
    # move file
    shutil.move(src_folder + file_name, new_name)
else:
    shutil.move(src_folder + file_name, dst_folder + file_name)
Move All Files From A Directory
Sometimes we want to move all files from one directory to another. Follow the below steps to move all files from a directory.

Get the list of all files present in the source folder using the os.listdir() function. It returns a list containing the names of the files and folders in the given directory.
Iterate over the list using a for loop to get the individual filenames
In each iteration, concatenate the current file name with the source folder path
Now use the shutil.move() method to move the current file to the destination folder path.
Example: Move all files from the report folder into a account folder.

import os
import shutil

source_folder = r"E:\pynative\reports\\"
destination_folder = r"E:\pynative\account\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
Our code moved two files. Here is a list of the files in the destination directory:

profits.txt
revenue.txt
expense.txt
Use the os.listdir(dst_folder) function to list all files present in the destination directory to verify the result.

Move Multiple Files
Let’s assume you want to move only a few files. In this example, we will see how to move files present in a list from a specific folder into a destination folder.

import shutil

source_folder = r"E:\pynative\reports\\"
destination_folder = r"E:\pynative\account\\"
files_to_move = ['profit.csv', 'revenue.csv']

# iterate files
for file in files_to_move:
    # construct full file path
    source = source_folder + file
    destination = destination_folder + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)
Output:

Moved: profit.csv
Moved: revenue.csv
# Move Files Matching a Pattern (Wildcard)