# more messing with functions
# anonymous functions

# author: gerry callaghan

'''
x = lambda arg1: arg1**2

answer = x(4)

# we can print as follows
# print(f"{answer}")

# but as print is one function, we can pass a variable to the lambda function 
# and the output to the print function as follows
print(f"{x(4)}")
'''

'''
#business_type = "standard"
business_type = "reduced"

vatcalc = lambda amount: amount * 0.23

if business_type == "reduced":
    vatcalc = lambda amount: amount * 0.135

cash = 10
print(f"{vatcalc(cash)}")
'''

'''
# sort a list
numbers = [2,33,55,1,4]

sorted_numbers = sorted(numbers)
print(f"{numbers} sorted are {sorted_numbers}")
'''


# sort dictionary

data = [{"first":"Guido", "last":"Van Rossum", "YOB": 1956},
         {"first":"Grace", "last":"Hopper", "YOB": 1906},
         {"first":"Alan", "last":"Turing", "YOB": 1912}]

'''
#this won't work
sorted_data = sorted(data)

print(f"{data} sorted are {sorted_data}")
'''

#instead we need to write it as follows, where we pass in x and get back YOB
sorted_data = sorted(data,key=lambda x: x["YOB"])

#the following works but prints out too much together
# print(f"{data} sorted are {sorted_data}")

for item in sorted_data:
    print(f"{item}")

data = [{"first":"Guido", "last":"Van Rossum", "YOB": 1956},
         {"first":"Grace", "last":"Hopper", "YOB": 1906},
         {"first":"Alan", "last":"Turing", "YOB": 1912}]

sorted_data2 = sorted(data,key=lambda x: x["first"])

for item in sorted_data2:
    print(f"{item}")