# Open notes.txt, read its content, and print it to the console.

file=open("notes.txt","r")

content=file.read()
print(content)

file.close()