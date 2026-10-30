'''Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)'''

import shutil

# shutil.copy("tasks.txt","new_dir/")
# shutil.move("notes.txt","new_dir/")

shutil.rmtree("new_dir")

