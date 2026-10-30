# Write a program that writes three lines of text to a file tasks.txt.

file=open("tasks.txt","w")

text='''Hii,myself Atharv
i love to write code in python
it easy to understand'''

file.write(text)

file.close()