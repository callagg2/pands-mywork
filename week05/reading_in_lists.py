# this program reads in the data for the data structure above, ie
# reads in a student’s name, then keeps reading in their modules and grades
# until the user enters a blank module name

student =str(input("Please enter the student's name: ")) 
module = str(input("Please enter the student's module: (Press q to quit) ")) 
grade = str(input("Please enter the student's grade"))



student = { 
"name":"Mary", 
"modules": [ 
{
"courseName":"Programming", 
"grade": 45 
},
{
"courseName":"History", 
"grade":99  
}
]
}




while module != "q":
    student.append((modules,rangeto))



print ("Student: {}".format(student["name"]))
# or
print(f"Student: {student["name"]}")

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
    print(f"\t {module["courseName"]} \t:{module["grade"]}")