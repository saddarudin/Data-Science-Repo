# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell
# you in which month that expense occurred. If expense is not found then
# it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
amount = int(input("Enter expense amount: "))
if amount == expense_list[0]:
    print("It is January's expenditure")
elif amount == expense_list[1]:
    print("It is February's expenditure")
elif amount == expense_list[2]:
    print("It is March's expenditure")
elif amount == expense_list[3]:
    print("It is April's expenditure")
elif amount == expense_list[4]:
    print("It is May's expenditure")
else:
    print("Not found in any month.")

