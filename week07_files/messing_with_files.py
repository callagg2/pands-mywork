# messing with files

#author: Gerry Callaghan

FILENAME="data.txt"

'''
#often we want to read in text mode rather than binary to prevent any executibles
# so we would write with open(FILENAME, "rt") as f: so yes rt instead of just r
with open(FILENAME, "r") as f:
    data = f.read()
    print(data)
    #if we wantthe first character of the file, we would say print(data[0])
    print(data[0])
# if you want toread out one line at a time, you would write
# for data in f:  followed by print(data)
'''

'''
with open(FILENAME, "r") as f:
    for data in f:
        print (data)
        # note that print adds a new blank line, it's implicit in the print function 
        # so to avoid a new line being added, you write the following
        print (data, end="")
        # alternatively you could strip the data 
        print(data.strip())
'''

# now to write to a new file
with open("data2.txt","wt") as f:
    f.write("how now,\n ")
    f.write("brown cow")

''''''
# now to append to an existing file
with open("data2.txt","a") as f:
    f.write("what the hell ")
''''

''' 
# now to append to an existing file
with open("data2.txt","w+") as f:
    f.write("what the hell ")
    # be careful after you write to a file, the cursor will be at the end of the file
    # # so move it to the start
    f.seek(0)
    data = f.read()
    print(data)

'''
with open(data2.txt, "r") as f:
    data = f.read()
   
'''