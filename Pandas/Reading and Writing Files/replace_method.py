import pandas as pd
import numpy as np

df = pd.read_csv('weather_data.csv')
df.replace(to_replace=['', 'na'], value=np.nan)
print(df)