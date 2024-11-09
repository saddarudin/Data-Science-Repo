import pandas as pd

df = pd.read_csv('movies.csv')
print("All movies between 2000 and 2011")
print(df[(df.release_year > 2000) & (df.release_year <2011)])
