# this program makes a list that has say 10 random numbers (20000 - 80000)

# author: gerry callaghan
'''
import numpy as np

minsalary = 20000
maxsalary = 80000
number_of_entries = 10

salaries= np.random.randint(minsalary,maxsalary,number_of_entries)

print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries}")

'''
'''
# now let's run the above script but this time force the numbers to be the same, we do this using seed function
import numpy as np

minsalary = 20000
maxsalary = 80000
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)

print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries}")
'''
'''
# now modify the above script to make another array of numbers that has salaries plus 5000
import numpy as np

minsalary = 20000
maxsalary = 80000
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)

print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries}")

salaries_plus = salaries + 5000
print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries_plus}")
'''
# now modify the above script to make another array of numbers that has salaries plus 5000
import numpy as np

minsalary = 20000
maxsalary = 80000
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)

print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries}")

salaries_plus_five_percent = salaries * 1.05
print(f"A list of 10 random numbers between 20,000 and 80,000 is:  {salaries_plus_five_percent}")

# By multiplying by 1.05 we now have floats, convert to an int array (using a floor)
new_salaries= salaries_plus_five_percent.astype(int)
print(f"A list of 10 random numbers between 20,000 and 80,000 in INT form is:  {new_salaries}")