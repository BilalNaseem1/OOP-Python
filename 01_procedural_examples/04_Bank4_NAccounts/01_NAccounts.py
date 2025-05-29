account_names = []
account_balances = []
account_passwords = []

# Account number would be index

def make_account(name, balance, password):
    account_names.append(name)
    account_balances.append(balance)
    account_passwords.append(password)

def show_account(accountNumber):
    print('Showing Account Details')
    print(f"        Account Name: {account_names[accountNumber]}")
    print(f"        Account Balance: {account_balances[accountNumber]}")
    # print(f"        Account Name: {account_passwords[accountNumber]}")
    print()

def getBalance(accountNumber, password):
    if password != account_passwords[accountNumber]:
        print('Incorrect password')
        print()
        return None
    else:
        balance = account_balances[accountNumber]
        print()
        return balance

# creating a sample account
make_account('Bilal', 100000, 'xxx')
make_account('Jolie', 100, 'ppp')

while True:
    print()
    print('press b to get balance')
    print('press d to deposit')
    print('press q to quit')
    print()

    user_input = input("What would you like to do? \n")[0].lower()

    if user_input not in ('b', 'd', 'q'):
        print()
        print("Invalid input bro!, Please try again")
        continue

    if user_input == 'b':
        account_number = int(input("Please enter your account number:\n"))
        account_password = input("Please enter your account password:\n")

        if account_password in account_passwords and account_number < len(account_names):
            balance = getBalance(account_number, account_password)
            if balance is not None:
                print(f"Your Account Balance is: {balance}")
        else:
            print("Invalid Account Name or password")
    if user_input == 'd':
        print("Deposit functionallity not available for now")
        continue

    if user_input == 'q':
        print("Quitting the game!")
        print()
        break



