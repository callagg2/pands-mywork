# this file contains all the utility functions that will be called in lab_original

#author: gerry callaghan

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