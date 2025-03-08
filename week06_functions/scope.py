# more messing with functions
# variable scope

#author: gerry callaghan

# don't use global variables and here is why!

x = 999 

'''
def fun():
    print(x)

fun()'
'''
# this is better 
# - use another variable within the function, you can still pass in x from outside as follows
# note we need to say fun(x) because the function fun(num) now expects aa variable

def fun(num):
    print(num)

fun(x)

# now we are going to show how if you change the variable value inside the function
# it can be confusing

def fun2(x):
    print(F"in fun2 x is {x}")
    x = 21
    print(F"in fun2 x is {x}")

fun2 (x)
print(F"after fun2 x is {x}",end="\n\n")

# this would be better to use say x2
def fun2(x2):
    print(F"in fun2 x is {x2}")
    x2 = 21
    print(F"in fun2 x is {x2}")

fun2 (x)
print(F"after fun2 x is {x}",end="\n\n")

# let's say we want to change the global value, this is how we write it

def fun2(x2):
    print(F"in fun2 x is {x2}")
    global x
    x = 21
    print(F"in fun2 x is {x2}")

fun2 (x)
print(F"after fun2 x is {x}")