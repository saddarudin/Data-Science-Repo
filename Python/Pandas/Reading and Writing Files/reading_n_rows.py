import pandas as pd
# reading only 5 rows
df = pd.read_csv('scores.csv', header=1, names=['runs'], nrows=5)
print(df)
