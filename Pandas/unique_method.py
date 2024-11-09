import pandas as pd

df = pd.read_csv('movies.csv')
print("Looking for unique industries...")
print(df.industry.unique())
print("How many unique languages are there?")
print(df.language.unique())
