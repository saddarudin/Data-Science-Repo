import pandas as pd

df1 = pd.DataFrame({
    'city': ['Dadu', 'Jamshoro', 'Larkana', 'Matiari', 'Khairpur'],
    'temperature': [43, 37, 47, 35, 44]
})

df2 = pd.DataFrame({
    'city': ['Dadu', 'Jamshoro', 'Larkana', 'Matiari', 'Khairpur'],
    'humidity': [65, 55, 70, 45, 65]
})

# axis = 1 means concat column wise not row wise (axis=0 which is by default means row wise)
df3 = pd.concat([df1, df2], axis=1)
print(df3)
