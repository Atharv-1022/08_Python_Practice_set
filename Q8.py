'''Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

python count_lines.py tasks.txt'''
import sys

def count_line(filename):
    with open(filename) as file:
        return len(file.readline())

if __name__=="__main__":
    filename=sys.argv[1]
    num_lines=count_line(filename)
    print(f"There are {num_lines} in file {filename}")