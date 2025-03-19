# mesing with histograms

# author: gerry callaghan

import numpy as np
import matplotlib.pyplot as plt

# to ensure to get the same numbers again, seed your data
#np.random.seed(1)
'''
#normal distribution
norm_data= np.random.normal(size=100000)

plt.hist(norm_data)
plt.show()

'''
# pie chart
fruit = np.array(["apples", "oranges","bananas"])
numbers=np.array([12,77,500])

plt.pie(numbers, labels=fruit)
plt.legend()
plt.show()