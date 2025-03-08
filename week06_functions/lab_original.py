# this sorts the array we store everything in

# author: gerry callaghan

# now we're going to put these functions into anther file and call them in
'''
def display_menu():
    print(f"what would you like to do?")
    print(f"\t(a) Add new student")
    print(f"\t(v) View students")
    print(f"\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

def do_add(students):
    current_student = {}
    current_student["name"]=input("Enter name :")
    current_student["modules"]= read_modules()
    students.append(current_student)

def read_modules():
    modules =[]
    module_name = input("\tEnter the first module name (blank to quit): ")

    while module_name != "":
        module = {}
        module["name"]=module_name
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        #now read the next module name
        module_name = input("\tEnter next module name (blank to quit)")
    return modules

def display_modules(modules):
    print("\tName\tGrade")
    for module in modules:
        print(f"\t{module["name"]}\t{module["grade"]}")


def do_view(students):
    for current_student in students:
        print(f"{current_student["name"]}")
        display_modules(current_student["modules"])
'''

import student_util as su
#main program
students = []

choice = su.display_menu()
while (choice != "q"):
    #we could do this with lambda functions
    # I am keeping this basic for the moment
    if choice =="a":
        su.do_add(students)
    elif choice == "v":
        su.do_view(students)
    elif choice != "q":
        print(f"\n\nPlease select either a, v, or q")
    choice= su.display_menu()        

