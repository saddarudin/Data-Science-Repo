import pandas as pd
"""
There are two ways to access columns using df
1. df[column_name]
2. df.column_name
"""
df = pd.read_csv('sample.csv')
print(f"Minimum score is: {df.scores.min()}")
print(f"Maximum score is: {df.scores.max()}")
print(f"Average score is: {df.scores.mean()}")
