# Messing with Functions
# to demonstrate the defining and using functions 
# author: gerry Callaghan

'''
# 2 ways of writing print
x, y, z = (1, 2, 3)
#print(x,y,z)
print(f"{x},{y},{z}",sep="", end="")
print(x,y,z,sep="", end="")
print(x,y,z,sep=",", end="\n")
#print(f"x,y,z is {x}-{y}-{z}")

'''

# Let's define a function
'''
def cube(number):
    # print(number)
    return (number **3)
'''

'''
ans = cube(23)
print(f"we got an answer of: {ans}")
'''

'''
ans = cube(33)
print(f"we got an answer of: {ans}")
# or write it as 
print(f"and 33 cubed is: {cube(33)}")

num = 45
print(f"and {num} cubed is: {cube(num)}")
'''

# we set the default of the power to be 3 because we are only passing one variable from our print function
def power_of(number,power=3):
    # print(number)
    return (number **power)

num = 45
print(f"and {num} cubed is: {power_of(num)}")
# here we pass in a power of 2, yes it does still say cubed but ignore that
print(f"and {num} cubed is: {power_of(num,2)}")
