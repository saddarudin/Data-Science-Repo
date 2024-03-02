import pandas as pd

df = pd.read_csv("tweets.csv")
print(f"Shape of tweets.csv is: {df.shape}")
# print("First five lines from head.....")
# print(df.head(5))
# print("Last five lines ....")
# print(df.tail(5))
# print("Randomly printing five lines...")
# print(df.sample(5))
print("Printing text column")
print(df.Text)
print("Looking for column names")
print(df.columns)
