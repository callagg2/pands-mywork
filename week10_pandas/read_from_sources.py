# In this program I look at various ways of reading in data from lists

# author: gerry callaghan

import pandas as pd

# reading in dictionary objects
# the attribute names will be column names
# the index is automatically made
'''
data_as_dict_of_list = {
    "Name": [
        "Braund, Mr Owen Harris",
        "Allen, Mr William Henry",
        "Bonnell, Miss Elizabeth",
    ],
    "Age": [
        22,
        35,
        58
    ],
    "Sex": [
        "male",
        "male",
        "female"
    ],
}

df = pd.DataFrame(data_as_dict_of_list)
#df = pd.DataFrame(data_as_dict_of_list, index=["a", "b", "c"])

#print (df)
print(df.describe ())


# or a dictionary containing three sub-dictionaries
data_as_dict_of_list = {
    "Name": {
        "101": "Braund, Mr Owen Harris",
        "102": "Allen, Mr William Henry",
        "103": "Bonnell, Miss Elizabeth",
},
    "Age": {
        "101": 22,
        "102": 35,
        "104": 58 # purposely putting this in a different row to show
    },
    "Sex": {
        "101": "male",
        "102": "male",
        "103": "female"
    },
} 

df=pd.DataFrame(data_as_dict_of_list)
print(df)
'''

# or with just lists
data_as_lists = [
    [1,2,100,"male"],
    [2,4,100,"male"],
    [3,8,100,"female"],
]

#df = pd.DataFrame(data_as_lists)
# if we want to set the column names, we can do so as follows
df=pd.DataFrame(data_as_lists, columns=["x","y","percent","sex"])

print(df)


