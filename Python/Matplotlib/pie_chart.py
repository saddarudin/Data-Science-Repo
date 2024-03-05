import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('linechart.xlsx')

# calculate total sale of each item in the file
total_sale = df[['Fridge', 'Dishwasher', 'Washing Machine']].sum()
plt.pie(total_sale, labels=total_sale.index, autopct='%1.2f%%')
plt.show()
