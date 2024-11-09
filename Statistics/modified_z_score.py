"""
Modified z score uses median instead of mean in its base
modified_z = 0.6745*(x-median(x))/MAD
where MAD(Median Absolute Deviation) = median(|x-median(x)|)
"""
import numpy as np
import pandas as pd

df = pd.read_csv('movie_revenues.csv')

# Before calculating MAD let's first convert revenue in millions
df["revenue_mln"] = df.revenue.apply(lambda x: x/1000000)


# now for calculating MAD we are defining function to do that
def get_mad(s):
    median = np.median(s)
    diff = abs(s-median)
    return np.median(diff)


median_x = np.median(df.revenue_mln)
MAD = get_mad(df.revenue_mln)
df['modified_z_score'] = 0.6745*df.revenue_mln.apply(lambda x: (x-median_x)/MAD)
print(df[df.modified_z_score>3.5])

