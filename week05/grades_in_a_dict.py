# a program that stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data.

student = { # this is tuple where we can have terms with colon 
"name":"Mary", # the name is the first element
"modules": [ # the module is the second element, and it can be one of two variables so a list
{
"courseName":"Programming", # the first in this module is a tuple is programming
"grade": 45 # the second in this tuple is the grade of that program
},
{
"courseName":"History", # the second in this module is a tuple is history
"grade":99  # the second in this tuple is the grade of that program
}
]
}

print ("Student: {}".format(student["name"]))
# or
print(f"Student: {student["name"]}")

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
    print(f"\t {module["courseName"]} \t:{module["grade"]}")