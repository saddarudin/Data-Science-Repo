import pandas as pd
from matplotlib import  pyplot as plt

df = pd.read_excel('linechart.xlsx')

df.plot(kind='bar', x='Quarter')
# to rotate titles of x axis
plt.xticks(rotation=45)
plt.show()
