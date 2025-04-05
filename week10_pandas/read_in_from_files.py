# this script shows how to read in data from files

#author:gerry callaghan

import pandas as pd
import re
import numpy as np
import data_manipulation

filename="originalData.tsv"
workbookFilename = "timetableData.xlsx"
df = pd.read_table(filename)

df.to_excel(workbookFilename, sheet_name="activities", index=False)


ds_staff = data_manipulation.get_series_of_unique(df,"Staff (delimited)")

print(ds_staff) 

# use a different engine (openpyxl) to append to the book
with pd.ExcelWriter(workbookFilename, engine="openpyxl", mode="a") as writer:
    ds_staff.to_excel(writer, sheet_name="staff", index=False)

