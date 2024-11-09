"""
Peter Pandey is the owner of a popular hotel located in Bangalore.
He keeps a CSV file called **'food_db.csv'** that contains a comprehensive
list of food items available at his hotel. The database contains information
such as a unique food_id, name, discount, price, and rating for each food item.
Peter is currently planning to update the food database and make some changes
to the existing values. To accomplish this task, he seeks your help and
expertise to perform the following tasks.

- Read the csv file 'food_db.csv' and store it in variable 'df'.
- print the number of rows and columns in it
- show the dataframe


- Replace the 5% and 10% discounts to 13% inorder to attract more customers
- store the results in a variable 'new_df'
- show the dataframe 'new_df'


- Replace the categorical column 'rating' with corresponding numerical values.
- Criteria: ['Excellent': 4, 'very Good': 3, 'Good': 2, 'Average': 1]
- store the results in a variable 'new_df'
- show the dataframe 'new_df'
"""

import pandas as pd

df = pd.read_csv('food_db.csv')
r, c = df.shape
print(f"Number of rows: {r} \n Number of columns: {c}")
print(df)
new_df = df.replace({
    'discount': ['5%', '10%']},
    '13%'
)
# new_df=df.replace(to_replace=['5%', '10%'], value='13%')
print(new_df)

new_df = df.replace(['Excellent', 'Very Good', 'Good', 'Average'], [4, 3, 2, 1])
print(new_df)
