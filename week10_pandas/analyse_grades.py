# in this program I do some basic analysis of the grades.csv
# author: gerry callaghan


import pandas as pd
path = "/home/gerry/Downloads/Data_Analytics_Course/pands/pands-mywork/week_10_pandas/data/"

filename_for_grades = path + "grades.csv"

df = pd.read_csv(filename_for_grades, index_col=0)

#remove the rows with incomplete data
df.dropna(inplace=True)

#remove duplicates
df.drop_duplicates(inplace=True)

print(df)

mean_values = df.groupby("subject").mean()

print(mean_values)