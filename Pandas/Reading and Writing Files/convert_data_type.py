import pandas as pd

df = pd.read_csv('weather_data.csv', parse_dates=['day'])

print(df.day)
