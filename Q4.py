# Open tasks.txt in append mode and add a new line "Task Completed!".

file=open("tasks.txt","a")

text='''
Task Completed'''

file.write(text)

file.close()
