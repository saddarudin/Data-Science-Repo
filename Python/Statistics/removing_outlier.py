# Use this air bnb new york city data set and remove outliers using percentile
# based on price per night for a given apartment/home. You can use suitable upper
# and lower limits on percentile based on your intuition. Your goal is to come up
# with new pandas dataframe that doesn't have the outliers present in it.

import pandas as pd

df = pd.read_csv('AB_NYC_2019.csv')
percentile_99 = df.price.quantile(0.999)
percentile_1 = df.price.quantile(0.01)
new_df = df[(df.price <= percentile_99) & (df.price>= percentile_1)]
print(new_df.shape)
