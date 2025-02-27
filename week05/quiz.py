# this is a quiz

# author: gerry callaghan

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
    }
            ]
}

print(f"numberOfQuestions is a: {type(numberOfQuestions)}")
print(f"averageAge is a: {type(averageAge)}")
print(f"debugMode is a: {type(debugMode)}")
print(f"name is a: {type(name)}")
print(f"ages is a: {type(ages)}")
print(f"months is a: {type(months)}")
print(f"first element in months is a: {type(months[1])}")
print(f"book is a: {type(book)}")
print(f"stuff is a: {type(stuff)}")
print(f"second element of stuff is a: {type(stuff[2])}")
print(f"someone is a: {type(someone)}")
print(f"firstname is a: {type(someone["firstname"])}")
print(f"me is a: {type(me)}")
print(f"the teaching element in me is a: {type(me["teaching"])}")
print(f"the first semester is: {type(me["teaching"][0]["semester"])}")
print(f"the first coursename is: {type(me["teaching"][0]["courseName"])}")


