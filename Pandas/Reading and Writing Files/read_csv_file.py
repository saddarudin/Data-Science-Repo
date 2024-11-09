import pandas as pd

"""
skiprows will skip the number of rows you provide
but header will consider that row as header that you provide in parameter
"""
# df = pd.read_csv('scores.csv', skiprows=1)
# here second row will be the header because first row is 0 and second is 1 and so on.
df = pd.read_csv('scores.csv', header=1)
print(df)

