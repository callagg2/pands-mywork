# messing with functions, looking at their interface

# flexible arguments
# author: gerry callaghan

#you can write the objects in any other, it does not matter
print (1,2,3, end="\t", sep="," )

'''
# unnamed arguments
def fun1 (*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a","b","c")
'''
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for val in kwargs:
        print(val)

fun2(name="joe",age =21,gender="M")

# sample code
def ave(*values):
    number_of_values = len(values)
    sum = 0
    for value in values:
        sum = sum + value
    average = (sum / number_of_values)
    return average, sum


# this didn't work
 #print(f"the average of these numbers is {av1, sum_of_numbers= ave(1,2,3,4,5,6)}")

# if you look at return above, it returns two variables the first goes into av1 and the second goes into sum, while (1,2,3,4,5,6) are passed to ave function
av1,sum_of_numbers = ave(1,2,3,4,5,6)

print(f"{av1} and the sum is {sum_of_numbers}")