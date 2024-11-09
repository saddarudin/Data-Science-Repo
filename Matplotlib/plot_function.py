import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('linechart.xlsx')
# --> to set the size of the frame
plt.figure(figsize=(12, 4))
plt.plot(df.Quarter, df.Fridge, color='green', label='Fridge')
plt.plot(df.Quarter, df.Dishwasher, color='yellow', label='Dish Washer')
plt.plot(df.Quarter, df['Washing Machine'], color='red', label='Washing Machine')
# title of the graph
plt.title('Product Sales')
# Adding Y text on Y Axis
plt.ylabel('Revenue (in million dollars)')
# Adding text on X Axis
plt.xlabel('Financial Quarter')
# Showing titles of lines
plt.legend()
plt.show()
