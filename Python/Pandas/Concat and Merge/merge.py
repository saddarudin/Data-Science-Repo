import pandas as pd

df1 = pd.DataFrame({
    'city': ['Dadu', 'Matiari', 'Khairpur', 'Larkana'],
    'temperature': [34, 35, 38, 40]
})

df2 = pd.DataFrame({
    'city': ['Dadu', 'Matiari', 'Khairpur', 'Larkana'],
    'humidity': [62, 40, 61, 63]
})

df3 = pd.merge(df1, df2, on='city')
print(df3)
