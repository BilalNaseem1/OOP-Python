from Account import *

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")
print(oJoesAccount.show())

oJoesAccount.deposit(50, 'JoesPassword')
print(oJoesAccount.show())


# creating another account
print()

user_name = input("Please enter your account name to be created")
user_balance  = int(input("Please enter the amount of balance to start with"))
user_pswd = input("please enter your account password")

user_account = Account(user_name, user_balance, user_pswd)

print(user_account.show())