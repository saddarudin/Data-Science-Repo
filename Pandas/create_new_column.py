import pandas as pd

# create a new column  rbr revenue budget ratio (revenue/budget)

df = pd.read_csv('movies.csv')
df['rbr'] = df['revenue']/df['budget']
print(df)
