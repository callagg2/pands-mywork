# messing with the os module

#author: gerry callaghan

# import the module
import os

'''
# this opens another file in the SAME directory
FILENAME="messing_with_files.py"

#if it's up a directory, you would say
FILENAME="../messing_with_files.py"

# this check if it exists, and if it does, it prints it out, notice tne end="" 
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line,end="")
else:
    print(FILENAME,"does not exist")            
'''
os.remove("data2.txt") 
