"""
When few values are very high and other in comparison are very low then on plotting
their graph seems similar and difference is not seen clearly this is where we use
logarithm to see the difference between smaller values
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('income.csv')
df.plot(x='company', y='revenue', kind='bar', logy=True)
plt.show()

