import pandas as pd
import seaborn as sb

df = pd.read_excel('histograms.xlsx')
sb.histplot(df.Exam_Score)

