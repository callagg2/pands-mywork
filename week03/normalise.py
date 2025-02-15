# This program reads in a string.


#
# Author: Gerry Callaghan

raw_string = input("Please enter a string:")

# It also strips any leading or trailing spaces and converts all the letters to lower case.
normalised_string = raw_string.strip().lower()

# It then outputs the lengths of the original string 
length_of_raw_string = len(raw_string)

# It then outputs the lengths of the normalised string 
length_of_normalised_string = len(normalised_string)

#prints the normalised string
print(f"That String normalised becomes:{normalised_string}")
print(f"We reduced the input string from {length_of_raw_string} to {length_of_normalised_string} characters")