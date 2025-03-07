# read in two numbers and multiply them

# author: gerry Callaghan

# problem with these is that there is a lot of duplication
'''
num1 = False

while (num1 == False):
    try:
        num1 = int(input("Enter in the first number: "))
    except ValueError:
        print("That was not a valid number. ",end = "")
    
    #num1 = int(input("No strings, a number please: "))

try:
    num2 = int(input("Enter in the second number: "))
except ValueError:
    num2 = int(input("No strings, a number please: "))


answer = num1*num2
print(f"{answer}")
'''
# replace the above with the use of a function

def read_num(message= "Enter a number:"):
    num = False
    while (not num): # we could have said num == False
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a valid number. ",end = "")
    return num

num1 = read_num()
# so we are going to pass a variable of "enter num2" to override the default of "Enter a number"
num2 = read_num("enter num2:")

answer = num1*num2
print(f"{answer}")