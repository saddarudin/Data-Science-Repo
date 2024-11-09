import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('histograms.xlsx')

plt.hist(df.Exam_Score)
plt.show()
