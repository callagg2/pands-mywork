# this is the lab on pandas for week 10

# author: gerry callaghan

import pandas as pd
'''
Create a dataframe (df) with data in it. You may use 
Dict with lists, 
Dict with dict, or 
list with list 
Print out the dataFrame. 
(I am using list with list, but setting the column names). 
You can use head to just print out the first 3 rows
'''


list_data= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(list_data, columns=['name','subject','grade'])
print(df.head(3))

'''Use the describe function to see the overall stats on the grades (use the type
function to see that this output is a dataframe'''

print(df.describe())
print(type(df.describe()))

'''Write this dataframe to a csv file called grades.csv (look at the csv file, why does
the first line start with a comma'''

#i'm telling the compiler where to put the file
path = "/home/gerry/Downloads/Data_Analytics_Course/pands/pands-mywork/week_10_pandas/data/"
# i'm given the file a name
csv_filename= path + "grades2.csv"
#i'm saying write from dataframe (df) to the csv file we named above
df.to_csv(csv_filename)

'''And write it to an excel file called grades.xlsx (in sheet "data") without the index
column.'''

# so this is the file name 
excel_filename = path +'grades.xlsx'
#this is the command to write the dataframe (df) to the file name , and give the worksheet a name of data
#I'm going to say to skip the index at the beginning
df.to_excel(excel_filename, index=False, sheet_name='data')

'''Add the description to another sheet called "summary". You will need to change
the writer to open from the default writer. (if you get a permission denied, close
the workbook in excel)'''

with pd.ExcelWriter(excel_filename, engine="openpyxl", mode="a") as writer:
    df.describe().to_excel(writer,sheet_name="sumnmary")

'''Calculate and print the mean of the grades'''
#mean = df.describe().loc['mean','grade']
#print(mean)
# or
mean = df['grade'].mean()
print (mean)
