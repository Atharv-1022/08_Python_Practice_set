'''Write a command-line utility search_word.py that takes two arguments:

A filename
A word to search and prints how many times the word appears in the file.'''

import sys

def count_word(filename,words):
    with (open(filename,"r")) as file:
        text=file.read()
        word_list=text.split()
        count=0
        for item in word_list:
           if item==words:
            count+=1
        return count

if __name__=="__main__":
    filename=sys.argv[1]
    words=sys.argv[2]
    num_count=count_word(filename,words)
    print(num_count)



