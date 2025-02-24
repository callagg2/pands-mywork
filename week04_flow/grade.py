# this program reads in a number and prints out the corresponding grade

# author: Gerry Callaghan

nonrounded_percentage = float(input("Enter the percentage: "))
# numberToRound = float(input("Enter a float number:"))
percentage = round(nonrounded_percentage)
# print (percentage)

# be careful with the use of "and" and "or"

if (percentage < 0) or (percentage > 100):

# This should really throw an error unless you indent the if statement
    print ("Please enter a number between 0 and 100")

elif (percentage < 40): 
    ## we know it is greater than 0
    print (f"{percentage}% s a Fail")
elif (percentage < 50): 
    # between 40 and 49
    print (f"{percentage}% is a Pass")
elif (percentage < 60): 
    # between 50 and 59
    print (f"{percentage}% is a Merit1")
elif (percentage < 70): 
    # between 60 and 69
    print (f"{percentage}% is a Merit 2")
else: 
    # the only option left is between 70 and 100
    print (f"{percentage}% is a Distinction")

