import pandas as pd

df = pd.read_csv('weather_data.csv', na_values=['', 'na'])

"""
There are different methods of filling missing values
1. Fill a single value in all missing or NaN values:
df.fillna(value, inplace=True)

2. Filling particular column with particular value
df.fillna({'column_name': value, 'column_name': value, ...}, inplace = True)

3. Filling the value of previous cell (Forward Fill)
df.fillna(method='ffill', inplace=True)

4. Filling value of succeeding cell (Backward Fill)
df.fillna(method='bfill', inplace=True)

Note: If there are more than 1 missing values consecutively in a single column 
and if you will use ffill or bfill it will fill all the cells but you can limit 
it using: 
df.fillna(method='ffill', inplace=True, limit=<number of cells you want to fill>)

5. Filling cell with mean of the cells below it and above it 
e.g: 22 NaN 26 ... so NaN will be 24
df.interpolate(inplace=True)

6. Dropping the entire row: If NaN values are small compared to data set then 
instead of filling each value you can drop that record:
df.dropna(inplace=True)

Note: you can use 'how' attribute in dropping like:
how=any--> it will drop the row if it has any NaN value,
how=all--> it will drop the row if all of its cells contain NaN value
Syntax: df.dropna(how='any/all', inplace=True)
"""
df.dropna(inplace=True)
print(df)
