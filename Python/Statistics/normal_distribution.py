import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('weight-height.csv')
# height mean, std, +3sigma and -3sigma
df_height = df.Height
height_mean = df_height.mean()
height_std = df_height.std()
h_minus3 = height_mean-3*height_std
h_plus3 = height_mean+3*height_std


# weight mean, std, +3sigma and -3sigma
df_weight = df.Weight
weight_mean = df_weight.mean()
weight_std = df_weight.std()
w_plus3 = weight_mean+3*weight_std
w_minus3 = weight_mean-3*weight_std


height_no_outlier = df[(df_height>h_minus3) & (df_height<h_plus3)]
weight_no_outlier = df[(df_weight>w_minus3) & (df_weight<w_plus3)]

sns.histplot(height_no_outlier, kde=True)
plt.show()
