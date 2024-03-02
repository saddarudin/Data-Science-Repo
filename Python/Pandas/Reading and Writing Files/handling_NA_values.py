import pandas as pd

"""
The main purpose of doing so is to convert into actual NaN values in the entire sheet.
You can do this by two ways either specifying a column to make changes only that column
or make changes in entire dataset
"""

# making changes in entire dataset

# df = pd.read_csv('scores.csv', header=1, na_values=['na', 'not available', -1, ''])

df = pd.read_csv('scores.csv', header=1, na_values={
    'scores': ['na', 'not available', -1, '']
    # add more columns like above
})

print(df)
