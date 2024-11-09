import pandas as pd

df = pd.read_csv('weather_by_cities.csv')


def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return "other"


g = df.groupby(lambda x: grouper(df, x, 'temperature'))
for group, data in g:
    print(group)
    print(data)
