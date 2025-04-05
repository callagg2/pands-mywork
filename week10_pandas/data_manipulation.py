# this module is for manipulating data

# author: gerry callaghan

'''
this gets you a series of unique value from a column that contains 
some of the values in a delimited form
'''

import pandas as pd
import random
import re

def get_series_of_unique(dataFrame, name_of_col,delim='/'):
    #drop na gets rid of the values in the series that have no value
    #this actually returns a numpy.ndimensional array
    values_with_delimits = dataFrame[name_of_col].dropna().unique()

    #iterate through it and break up the delimited values
    # I am usng a set because set remove duplicates

    unique_values = set([]) # empty set
    for value_in_col in values_with_delimits:
        #print(staff,":",type(staff)) # for debugging
        values_as_list = re.split('/',value_in_col)
        unique_values.update(values_as_list)
    ds = pd.Series(list(unique_values))
    # i take the liberty of sorting this series
    ds.sort_values()
    return ds

'''
I am doing this to demonstrate adding a column, this function is essentially one line
It is only here so i can demonstrate it

'''


def add_column_addition(df, newCol ,col1, col2, delim=', '):
    # this could use the cat function or simple additions
    df[newCol] = df[col1] + delim + df[col2] 
    
    # I don't need to return df as it should be changed
    # but i am to allow chaining
    return df

'''
randomise data
based on Column'
'''

def randomise_data_on_col(df, columnName):
    oldSeries = get_series_of_unique(df, columnName)
    
    # I haven't checked whish is the quicker randomiser
    # pandas of lists
    oldList = oldSeries.tolist()
    randomise_data_on_list(df, oldList)

def randomise_data_on_list(df, oldList):
    newList = oldList.copy()
    random.shuffle(newList)
    #print(oldList) # debug checkig they are different
    #print(newList) # debug
    df.replace(oldList, newList, inplace=True, regex=True)

def clear_module_ids(module_name):
    # this code is taken from 
    # https://www.geeksforgeeks.org/replace-values-in-pandas-dataframe-using-regex/
    # we could have used replace

    # format XXXXDDDDD (x is letter D is number)
    regex = '^[a-zA-Z]{4}[0-9]{5} '
    if re.search(regex, module_name):

        # Extract the position of beginning of pattern
        #pos = re.search(regex, moduleName).end()

        # I know the size of what needs to be extracted
        return module_name[10:]

    else:
        # if clean up needed return the same name
        return module_name

def randomise_moduleN_names(df, column_name):
    old_series = get_series_of_unique(df, column_name)
    
    # strip out the module codes 
    # i could have done this by finding the list of module ids and replacing them with ''
    cleaned_series= old_series.apply(clear_module_ids)

    #print(cleanedSeries.tolist())  # debug
    randomise_data_on_list(df, cleaned_series.tolist())

def randomise_staff(df, df_fake_names):

    # format the fake names
    # randomise the order
    # from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
    df_fake_names = df_fake_names.sample(frac=1).reset_index(drop=True)
    # make the comma seperated name
    add_column_addition(df_fake_names, 'fullName', 'last', 'first')
    #print (df_fakeNames) # debug


    ds_staff =get_series_of_unique(df, 'Staff (delimited)')
    #print(ds_staff)
    #print(ds_staff.size)  # debug


    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
    # I had a few issues with this, it only liked lists for some reason
    # and it is matching the exact value in the element not subString, regex fixed this
    #df.replace(ds_staff.tolist(), df_fakeNames.fullName[:ds_staff.size].tolist(), inplace=True, regex=True)'
