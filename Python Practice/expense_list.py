# Let's say your expense for every month are listed below:
# i. January -2200
# ii. February -2350
# iii. March -2600
# iv. April - 2130
# v. May -2190

# Create a list to store these monthly expenses and using that find out,
monthly_expense = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January
extra_expenditure = monthly_expense[0]-monthly_expense[1]
print("In February extra expenditure compared to January was ", -extra_expenditure)

# 2. Find out your total expense in first quarter (First three months) of the year
quarterly_expenditure = monthly_expense[0]+monthly_expense[1]+monthly_expense[2]
print("Quarterly expenditure was of ", quarterly_expenditure)

# 3. Find out if you spend exactly 2000 dollars in any month
if 2000 in monthly_expense:
    print("Yes I spent exactly 2000$ in a month")
else:
    print("No I have not spent exactly 2000$ in any month")

# 4. June month just finished and your expense is 1980 dollar.
# Add this item to your monthly expense list
monthly_expense.append(1980)
print(monthly_expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$.
#    Make a correction to your monthly expense list based on this
monthly_expense[3]=monthly_expense[3]-200
print(monthly_expense)
