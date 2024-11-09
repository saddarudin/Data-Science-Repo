import pandas as pd
"""
new column can be created from one column or more than one columns
for example: we can calculate age of movies depending on the release year column
but if we want to calculate profit we need two columns revenue and budget
"""
df = pd.read_csv('movies.csv')
# creating new column depending on one column
df['age'] = df['release_year'].apply(lambda x: 2024-x)
print(df.head(10))
# creating new column depending on two columns
df['profit'] = df.apply(lambda x: x['revenue']-x['budget'], axis=1)
print(df.head(10))
print(df.columns)
