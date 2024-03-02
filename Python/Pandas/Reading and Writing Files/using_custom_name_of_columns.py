import pandas as pd

df = pd.read_csv('scores.csv', header=1, names=['runs'])
print(df)
