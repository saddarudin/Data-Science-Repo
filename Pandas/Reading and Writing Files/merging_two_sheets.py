import pandas as pd

df_movies = pd.read_excel('movies_db.xlsx', 'movies')
df_financials = pd.read_excel('movies_db.xlsx', 'financials')
df_merged = pd.merge(df_movies, df_financials, on='movie_id')

# saving merged file
df_merged.to_excel('merged_sheet.xlsx', 'movies', index=False)
