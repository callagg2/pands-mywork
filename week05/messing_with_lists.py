# this program just messes with lists

# author: gerry callaghan

boats = ["sigma", 23, [1,2,3], {}]
'''
boats = boats + [1,2,3]

boats = [2,6,3, 9, 4]

boats.append(8)

boats.sort (reverse = True)

for boat in boats:
    print(type(boat))
'''

''''
ages = [12, 21,23, 34]
sum = 0


for age in ages:
    sum = sum + age

print(sum)

L = [2,3,5,7,11]
print(L[-2])
print(L[:3])

string = "123456789"
print(string[-4:])
print(string[6::2])

L[4] = 12
print(L)

L[1:3] = [55,56]
print(L)
'''''

# TUPLES
t=(1,2,3)
# we now assign three variables the successive values in the tuple
x,y,z = t
print(z)

x = 0.125
# as.integer_ratio is a built in function
x.as_integer_ratio()

numerator, denominator = x.as_integer_ratio()
print(numerator,"/",denominator)
