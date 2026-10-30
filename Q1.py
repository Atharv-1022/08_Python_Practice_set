# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
import os

file=open("notes.txt","w")

text='''Learning python is fun!'''

file.write(text)

file.close()