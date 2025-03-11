# messing with csv files

# author: gerry callaghan

import csv
FILENAME="data3.csv"
'''
# reading from a csv file
with open(FILENAME, "rt") as file:
    csvReader = csv.reader(file,delimiter=",") # delimiter can be anything, in this case a comma
    for line in csvReader: # line will be a list containing the variables in each line
        age = line[2] # the age
        print(age) # note this is printing the header row, i provide a solution to this in the tutorial
'''

# writing to a csv file

mydict = [{"first":"Andrew", "last": "Beatty", "age":"21"},
          {"first":"Joe", "last":"Bloggs", "age":"22"},
          {"first":"Mary", "last":"Jones", "age":"33"}
          ]

#field names
fields = ["first","last","age"]

# name of csv file
FILENAME = "data3.csv"

# writing to csv filee
with open(FILENAME, "w", newline="") as csvfile:
    #creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

# writing headers (field names)
writer.writeheader()
for dictrow in mydict:
    print(dictrow)
    writer.writerow(dictrow)
