"""
- Read the 3 csv files provided into separate dataframes
(movies.csv to df_movies, financials.csv to df_financials, languages.csv to df_languages).
- show the top 3 rows for each dataframe.

- Read the csv file 'new_movies.csv' and store it into dataframe 'df_new_movies'
- Now, contact the dataframes[df_movies, df_new_movies] and store the results again to df_movies.
 Make sure to ignore the index while concatenating

- Merge the dataframe df_movies with the df_languages on 'language_id'.
- Make sure you perform a **inner** join here.
- Store the result again to df_movies

- Merge the dataframe df_movies with the df_financials on 'movie_id'.
- Make sure you perform a **left** join here.
- Store the result again to df_movies

- Save the 'df_movies' dataframe with name 'final_complete_data.csv'.
- Only take the columns 'movie_id', 'title', 'lang_name', 'budget', 'revenue', 'currency'
- set the index to False while saving the dataframe
"""

import pandas as pd

df_movies = pd.read_csv('movies.csv')
df_financials = pd.read_csv('financials.csv')
df_languages = pd.read_csv('languages.csv')

print(df_movies.head(3))
print(df_financials.head(3))
print(df_languages.head(3))

df_new_movies = pd.read_csv('new_movies.csv')

df_movies = pd.concat([df_movies, df_new_movies], ignore_index=True)

df_movies = pd.merge(df_movies, df_languages, on='language_id', how='inner')

df_movies = pd.merge(df_movies, df_financials, on='movie_id', how='left')

# Don't remove comment from below line it will create a new file that is already created!!!
# df_movies.to_csv('final_complete_data.csv',
#                  columns=['movie_id', 'title', 'lang_name', 'budget', 'revenue', 'currency'],
#                  index=False)
