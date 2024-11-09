import pandas as pd

"""
df.describe() will print some calculations for all numeric values
like: minimum, maximum, standard deviation, average etc
"""

df = pd.read_csv('movies.csv')
print(df.describe())
