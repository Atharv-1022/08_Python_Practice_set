'''Write a program that reads a file and creates another file with all words converted to uppercase'''
file=open("tasks.txt","r",)

content=file.read()

file.close()
f=open("new_file.txt","w")
f.write(content.upper())

f.close