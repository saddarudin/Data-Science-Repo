import pandas as pd

"""
info method will print information about data set like 
number of null entries etc
"""

df = pd.read_csv('movies.csv')
df.info()
