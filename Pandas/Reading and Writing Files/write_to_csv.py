import pandas as pd

df = pd.read_csv('scores.csv', header=1, na_values=['not available', 'na', -1, ''])
df['average'] = df['scores']/5

# now making new file and add whole content of df to it

df.to_csv('cricket.csv', index=False)
