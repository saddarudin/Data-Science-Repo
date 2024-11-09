import pandas as pd

"""
You can find maximum temperature of each city by three ways
1. df[df.city == 'mumbai'].temperature.max()

2. g=df.groupby('city') #---> separating data city wise 
   now run for loop to see max temp of each city
   
   for city, data in g:
       print(city, data.temperature.max())
       
3. g.max() ---> this will return maximum value of all the numerical columns in the data set
 similarly for min, mean, median etc

"""
df = pd.read_csv('weather_by_cities.csv')

g = df.groupby('city')
numeric = df.select_dtypes(include=['int', 'float']).columns
print(g[numeric].mean())

