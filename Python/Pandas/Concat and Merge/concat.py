import pandas as pd

"""
concat can take keys to differentiate between data frames
df.concat([df1, df2, df3, ...], keys=["key1", "key2"])

after that you can access data frames using its key like

df.loc["key1"]
"""
food = pd.read_csv('food.csv')
food_db = pd.read_csv('food_db.csv')

concat = pd.concat([food, food_db], ignore_index=True)
print(concat)
