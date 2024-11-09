# Create a class called BankAccount with attributes account_number and balance.
# Write methods deposit(amount) and withdraw(amount) to update the balance accordingly.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
        else:
            print("Please enter correct amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount<=self.balance:
                self.balance -= amount
                print("Your have successfully withdrawn "+str(amount))
            else:
                print("You do not have sufficient balance in your account to withdraw.")
        else:
            print("Please enter correct amount")


my_account = BankAccount(124, 5000)
print(f"Initial balance {my_account.balance}")
my_account.deposit(200)
print(f"After depositing 200: {my_account.balance}")
my_account.withdraw(6000)
print(f"After withdrawing 3000: {my_account.balance}")
