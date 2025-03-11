# messing with json files

# author: gerry callaghan

# json is a module that we import, just like "os"

#we want to focus on dump and load

import json
'''
electric_bill = {

    "name" : "Andrew",
    "amount": "999"
}

with open ("storeData.json", "wt") as f:
    json.dump(electric_bill, f) # writes the dictionary object to the file as a json object

'''
# i am assuming that json has already been imported

# assuming that the file storeData.json exists and contains json
with open("storeData.json", "rt") as f:
    # we're going to store all the information in a variable called readDict
    readDict = json.load(f) # reads the file and converts the JSON object into a list of dictionary
    #from readDict we're going to search for the variable of the tuple name
    #print(readDict["name"])
    print(readDict["amount"])
