import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv')
# z=(x-mean)/std
# let's do for Height only
height_mean = df.Height.mean()
height_std = df.Height.std()
df_no_outlier = df[((df.Height-height_mean)/height_std<3) & ((df.Height-height_mean)/height_std>-3)]

sns.histplot(df_no_outlier, kde=True)
plt.show()
