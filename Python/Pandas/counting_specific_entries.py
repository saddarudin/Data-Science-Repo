import pandas as pd

df = pd.read_csv('movies.csv')
print("How many bollywood and how many hollywood movies are there?")
print(df.industry.value_counts())
print("Number of movies based on language?")
print(df.language.value_counts())
