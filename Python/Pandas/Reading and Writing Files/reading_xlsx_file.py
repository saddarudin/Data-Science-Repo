import pandas as pd

df = pd.read_excel('movies_db.xlsx', 'movies')
print(df.head(5))
