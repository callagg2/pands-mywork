# messing with numpy
# author: gerry callaghan

import numpy as np
#import flask
#import flask -> to install a module, run conda activate, then pip install flask



list_of_numbers = [1,2,3,5,"asdf"]

print (f"the list is {list_of_numbers}")

numbers=np.array([1,2,3,4])
numbers = numbers + 3
print (f"the array is {numbers}")

numbers = numbers * 3
print (f"the array is {numbers}")

numbers = numbers - 3
print (f"the array is {numbers}")

rando = np.random.randint(100,200,30)
print(rando)
'''
normalrando = np.random.normal(size=100) # 100 random numbers around the mean of 0
print(normalrando)
'''
normalrando = np.random.normal(loc=50, scale=20, size=100)
print(normalrando)
