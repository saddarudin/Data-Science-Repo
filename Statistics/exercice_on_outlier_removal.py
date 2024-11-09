# You are given bhp.csv which contains property prices in the city of banglore, India.
# You need to examine price_per_sqft column and do following,
#
# 1. Remove outliers using percentile technique first.
#    Use [0.001, 0.999] for lower and upper bound percentiles.
# 2. After removing outliers in step 1, you get a new dataframe.
# 3. On step(2) dataframe, use 4 standard deviation to remove outliers
# 4. Plot histogram for new dataframe that is generated after step (3).
#    Also plot bell curve on same histogram
# 5. On step(2) dataframe, use zscore of 4 to remove outliers.
#    This is quite similar to step (3) and you will get exact same result.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# reading bgp.csv file
df = pd.read_csv('bhp.csv')


# Problem: 1 & 2
low_percentile = df.price_per_sqft.quantile(0.001)
high_percentile = df.price_per_sqft.quantile(0.999)
df_no_outlier = df[(df.price_per_sqft > low_percentile) & (df.price_per_sqft<high_percentile)]


# Problem: 3
price_mean = df_no_outlier.price_per_sqft.mean()
price_std = df_no_outlier.price_per_sqft.std()
minus4std = price_mean-4*price_std
plus4std = price_mean+4*price_std
df_no_outlier_std = df_no_outlier[(df_no_outlier.price_per_sqft<plus4std) & (df_no_outlier.price_per_sqft>minus4std)]


# Problem: 4

sns.histplot(df_no_outlier_std.price_per_sqft, kde=True)



# Problem: 5

z_mean = df_no_outlier.price_per_sqft.mean()
z_std = df_no_outlier.price_per_sqft.std()
df_no_outlier_z_score = df_no_outlier[(((df_no_outlier.price_per_sqft-z_mean)/z_std)>-4.0) & (((df_no_outlier.price_per_sqft-z_mean)/z_std)<4.0)]

sns.histplot(df_no_outlier_z_score.price_per_sqft, kde=True)
plt.show()
