import pandas as pd

df = pd.read_csv('weather_by_cities.csv')
g = df.groupby('city')
# for quick analysis of g
print(g.describe())
print(g.size())

