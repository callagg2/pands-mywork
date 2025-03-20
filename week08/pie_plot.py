# Demonstrate making a pie plot of the unique occurences of values in an array .
# I am demonstrating more than just how to do pie plots in this.

# author: gerry callaghan

import matplotlib.pyplot as plt
import numpy as np

'''
# make the array of occurences
possible_counties=("Waterford", "Tipperary", "Louth", "Donegal", "Leitrim", "Limerick", "Wicklow")

#pick 100 randomly from possible counties with the frequencies set in P
counties = np.random.choice(
    possible_counties,
    p=(0.1,0.2,0.3,0.1,0.1,0.1,0.1),
    size=(100)

)

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
plt.pie(counts, labels= unique)
plt.show()'
'''

# make the array of occurences
possible_counties=("Waterford", "Tipperary", "Louth", "Donegal", "Leitrim", "Limerick", "Wicklow")

#pick 100 randomly from possible counties with the frequencies set in P
counties = np.random.choice(
    possible_counties,
    p=(0.1,0.2,0.3,0.1,0.1,0.1,0.1),
    size=(100)

)

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
plt.bar(unique,counts)
plt.show()