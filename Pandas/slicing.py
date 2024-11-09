import pandas as pd

df = pd.read_csv("tweets.csv")
print("Print entries from 14 to 19")
print(df[14:20])
