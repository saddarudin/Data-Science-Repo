"""
When normal distribution is right skewed or left skewed then
to make it into normal distribution (bell curved) we use
logarithm it is called logarithm normal distribution
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('income2.csv', names=['income', 'count'], skiprows=1)
g=sns.barplot(x='income', y='count', data=df)
g.set(xscale='log')
plt.show()
