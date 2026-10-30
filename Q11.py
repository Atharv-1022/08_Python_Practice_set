# Create a script that deletes all .tmp files from the current directory using os and os.remove()

import os

for file in os.listdir("."):
    if file.endswith(".tmp"):
        os.remove(file)
        print(f"Deleted file {file}")