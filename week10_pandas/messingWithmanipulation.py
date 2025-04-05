# Showing how you read data from TSV files and outputting to excel
# Author: Gerry callaghan

import pandas as pd
import re
import numpy as np
import data_manipulation

filename = 'originalData.tsv'

df = pd.read_table(filename)

'''
#show the first two rows
You can this way
print(df[["Module ID", "Duration"]].head(2))
'''
# or this way
list_of_cols = ["Module ID", "Duration"]
print(df[list_of_cols].head(2))

# now something else - creating a column
df["new"] = df["Duration"] * df["Number of Weeks"]

list_of_cols = ['Number of Weeks', 'Duration', 'new']
#we only want to show the top 10 rows
print(df[list_of_cols].head(10))
