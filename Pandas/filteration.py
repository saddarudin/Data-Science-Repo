import pandas as pd
"""
From movies.csv filter out all the bollywood movies
"""
df = pd.read_csv('movies.csv')
df_b = df[df.industry=='Bollywood']
df_h = df[df.industry=='Hollywood']
print("All hollywood movies are ...")
print(df_h)
print("All bollywood movies are ...")
print(df_b)
