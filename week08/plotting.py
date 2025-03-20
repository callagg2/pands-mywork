# this programs plots a function of y = x-squared

# author: gerry callaghan

import matplotlib.pyplot as plt
import numpy as np

'''
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # mulitply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
'''
'''
minsalary = 20000
maxsalary = 80000
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)

plt.hist(salaries)
plt.show()
'''
'''
minsalary = 20000
maxsalary = 80000
low_age = 21
high_age=65
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)
ages = np.random.randint(low_age,high_age,size=number_of_entries)

plt.scatter(ages,salaries)
plt.show()
'''
minsalary = 20000
maxsalary = 80000
low_age = 21
high_age=65
number_of_entries = 10

np.random.seed(1)
salaries= np.random.randint(minsalary,maxsalary,number_of_entries)
ages = np.random.randint(low_age,high_age,size=number_of_entries)
plt.scatter(ages,salaries,label="Salaries")

#now we want to add a line y = x-squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, color="r", label="X-Squared")

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Ages")
plt.legend()


#plt.show()
plt.savefig("prettier-plot.png")