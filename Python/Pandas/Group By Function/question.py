# Here, the requirement is to create four groups based on **"imdb_rating"** use movies_data.csv
#
# - 1 <= imdb_rating <= 3.9 ---> 'Poor'
# - 4 <= imdb_rating <= 7.9 ---> 'Average'
# - 8 <= imdb_rating <= 10 --->  'Good'
# - If none of above satisfy, then return 'others'

import pandas as pd

df = pd.read_csv('movies_data.csv')


def grouper(df, idx, col):
    if 1 <= df[col].loc[idx] <=3.9:
        return 'Poor'
    elif 4 <= df[col].loc[idx] <= 7.9:
        return 'Average'
    elif 8 <= df[col].loc[idx] <= 10:
        return 'Good'
    else:
        return 'others'


g = df.groupby(lambda x: grouper(df, x, 'imdb_rating'))
for key, data in g:
    print("key: ", key)
    print("Data: ", data)
