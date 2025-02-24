# this program checks if a number is even

# author: Gerry Callaghan

number = int(input("Please enter an integer number:"))

# this is mod 2, so if mod 2 is zero it must be even
if (number % 2) == 0: 
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
## end if 

