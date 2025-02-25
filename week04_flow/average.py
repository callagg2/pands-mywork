# this program keeps reading numbers until the user enters a 0
# The program should then print out each of the numbers entered and the average of them. 

# author: gerry callaghan

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("Enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if it is 0
    number = int(input("Enter another number (0 to quit): "))

for value in numbers:
    print (value)

# we want the average to be float because the average is unlikely to be a round number

average = float(sum(numbers)) / len (numbers)
print(f"The average is: {average}")

