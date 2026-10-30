'''Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize()).'''
import os
import sys

folder=sys.argv[1]
total=0
for file in os.listdir(folder):
    file_path=os.path.join(folder,file)
    if os.path.isfile(file_path):
        size=os.path.getsize(file_path)
        total+=size


print(f"Total size of {folder} is : {total}")

