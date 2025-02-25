# this program generates 10 random numbers 
# The program should then print out the top three

# author: gerry callaghan

# I will use a list to store and manipulate the numbers

numbers =[]


import random

while len(numbers) <=9:
    number = random.randint(1, 100)
    numbers.append(number)

print(f"{len(numbers)} random numbers \t {numbers}")

# or from Peter, see the way he condenses 2 lines into 1
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100
numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))

    print (f"{howMany} random numbers\t {numbers}")

# so this bit i couldnt do as i didn't knwo about sort

# PEter "I am keeping the original list maybe I don't need to"
topOnes = numbers.copy() # so we are setting topOnes initially equal to a copy of numbers array

topOnes.sort(reverse = True) 
# so we now sort the array 
print (f"The top {topHowMany} are \t\t {topOnes[0:topHowMany]}") # so we choose the array, then say from the first to the variable tophow many



