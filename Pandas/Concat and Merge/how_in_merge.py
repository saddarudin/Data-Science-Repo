"""
There are four ways you can merge two tables
suppose you have two tables that have some common values and some values are different.

1. Inner Join: This will merge two tables and return a new table containing only common
               values of both tables.
2. Left Join: This will merge two tables and return a new table containing all the values
              of left table and common values in other table.
3. Right Join: This will merge two tables and return a new table containing all the values
               of right table and common values from other table.
4. Full Outer Join: This will merge two tables and return a new table containing all the values
              from both tables and values will not repeat.

syntax: merged_table = pd.merge(df1, df2, on='column_name', how='inner/left/right/outer')
"""

import pandas as pd

df1 = pd.DataFrame({
    'city': ['Dadu', 'Larkana', 'Khairpur', 'Matiari', 'Sukkur'],
    'temperature': [34, 38, 39, 30, 40]
})

df2 = pd.DataFrame({
    'city': ['Dadu', 'Larkana', 'Khairpur', 'Matiari', 'Karachi'],
    'humidity': [56, 57, 58, 58, 52]
})

df3 = pd.merge(df1, df2, on='city', how='outer')

print(df3)
