import pandas as pd

df = pd.read_csv('movies.csv')
# replacing index number with title column
df.set_index('title', inplace=True)
print(df.head(10))
# now you can access any movie using its index as name
print(df.loc['Pather Panchali'])
# you can access the data based on number using iloc (integer location)
print(df.iloc[1])
# to reset index
df.reset_index(inplace=True)
print(df.head(5))
