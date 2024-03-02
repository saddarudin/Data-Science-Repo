import pandas as pd

df = pd.read_csv('movies.csv')
"""
For printing subset of a data set two square braces are used
df[['column1','column2',...]]
"""
print('Print only title, industry and language columns')
print(df[["industry", "language", "title"]])
