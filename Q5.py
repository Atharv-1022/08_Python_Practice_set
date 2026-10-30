# Read the file and print all lines as a list using readlines().
file=open("tasks.txt","r")

for line  in file:
    print(line)

file.close()