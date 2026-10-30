'''Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder'''

import os

dir=os.getcwd()
print(f"the current directorys are {dir}")

list=os.listdir("08_Practice_set")
print(list)
os.mkdir("new_dir")