"""
1. How many men and women (sex feature) are represented in this dataset?
2. What is the average age (age feature) of women?
3. What is the percentage of German citizens (native-country feature)?
4-5. What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature)
     and those who earn less than 50K per year?
6. Is it true that people who earn more than 50K have at least high school education?
   (education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)
7. Display age statistics for each race (race feature) and each gender (sex feature).
   Use groupby() and describe(). Find the maximum age of men of Amer-Indian-Eskimo race.
8. Among whom is the proportion of those who earn a lot (>50K) greater: married or single men
   (marital-status feature)? Consider as married those who have a marital-status starting with Married
   (Married-civ-spouse, Married-spouse-absent or Married-AF-spouse), the rest are considered bachelors.
9. What is the maximum number of hours a person works per week (hours-per-week feature)?
   How many people work such a number of hours, and what is the percentage of those who earn a lot (>50K) among them?
10. Count the average time of work (hours-per-week) for those who earn a little and a lot (salary) for each country
    (native-country). What will these be for Japan?


    import pandas as pd
    df = pd.read_csv('../input/adult.data.csv')
    df.head()
    1.
    df.sex.value_counts()
    2.
    df[df.sex=='Female'].age.mean()
    3.
    germany_count = df['native-country'].value_counts().get('Germany')
    total_count = df['native-country'].count()
    percentage = (germany_count/total_count)*100
    percentage
    4-5.
    # Mean and standard deviation of age who earn more than 50K in year
    mean_age_more50 = df[df.salary == '>50K'].age.mean()
    # rounding off the answer to three decimal places
    mean_age1 = round(mean_age_more50,3)
    std_age_more50 = df[df.salary== '>50K'].age.std()
    std_age1 = round(std_age_more50,3)

    # Mean and Standard Deviation of age of those who earn less than 50K in a year
    mean_age_less50 = df[df.salary == '<=50K'].age.mean()
    mean_age2 = round(mean_age_less50,3)
    std_age2 = round(std_age_less50,3)
    std_age_less50 = df[df.salary == '<=50K'].age.std()
    print(f'Mean and Standard Deviation of age for those who earn more than 50K in a year is {mean_age1, std_age1}')
    print(f'Mean and Standard Deviation of age for those who earn less than 50K in a year is {mean_age2, std_age2}')

    6.
    print('It is false because see the below result')
    df[(df.salary == '>50K') & ((df.education != 'Bachelors') &
                            (df.education != 'Masters') &
                           (df.education != 'Prof-school') &
                           (df.education != 'Assoc-acdm') &
                           (df.education != 'Assoc-voc') &
                           (df.education != 'Doctorate'))]
    7.
    g = df.groupby(['race','sex'])
    age_statistics=g.age.describe()
    age_statistics.loc[('Amer-Indian-Eskimo', 'Male'), 'max']
    8.
    # total number of those who earn more than 50K

    total = len(df[df.salary == '>50K'])

    # Now those who earn more than 50K and are Married
    married = len(df[(df.salary == '>50K') & (df['marital-status'].str.startswith('Married'))])

    unmarried =  total-married

    print(f"Number of those who are married and earn more than 50K is {married} and for unmarried it is {unmarried}")

    9.
    max_hours = max(df['hours-per-week'])
    no_of_people = len(df[df['hours-per-week'] == max_hours])
    max_salary_max_hour=len(df[(df['hours-per-week'] == max_hours) & (df.salary == '>50K')])
    per = (max_salary_max_hour/no_of_people)*100
    per

    10.
    g = df.groupby(['native-country','salary'])
    average_time_per_country = g['hours-per-week'].mean()
    h = g['hours-per-week'].describe()
    Japan = h.loc['Japan', 'mean']

    print(f'For Japan average {Japan}\nFor all countries average: {average_time_per_country}')
"""

