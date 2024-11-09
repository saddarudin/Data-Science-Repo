# - Read the csv file 'fruits_data.csv' into the dataframe 'df'.
# - show the number of rows and columns in it.
# - list all the columns present in the dataframe.
# - show the dataframe

import pandas as pd

df = pd.read_csv('fruits_data.csv')
print(df.shape)
print(df.columns)
print(df)

# - Fill all the null values in the dataframe with '-1'
# and store the result to variable 'new_df'.

new_df=df.fillna(-1)
print(new_df)

# Fill the null values in respective columns like below:
# - apple(1 kg): Mean value of that column
# - banaba(a dozen): Mean value of that column
# - grapes(1 kg): Median value of that column
# - mango(1 kg): Median value of that column
# - Water Melon(1): Fill null values with "Not Available"
# Finally store the output to new_df variable


# before doing above code let's first use proper naming of the columns
df.rename(columns={
    'apple(1kg)': 'apple',
    'banana(1 dozen)': 'banana',
    'grapes(1kg)': 'grapes',
    'mango(1kg)': 'mango',
    'Water Melons(1)': 'water_melons'
}, inplace=True)

new_df=df.fillna({
    'apple': df.apple.mean(),
    'banana': df.banana.mean(),
    'grapes': df.grapes.median(),
    'mango': df.mango.median(),
    'water_melons': 'Not Available'
})

print(new_df)
