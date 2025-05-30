accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {
        'name': aName,
        'balance': aBalance,
        'password': aPassword
    }
    accountList.append(newAccountDict)

def show(accountNumber):
    print("Showing the details of the account")
    thisAccount = accountList[accountNumber]
    print(f"             Account Name: {thisAccount['name']}")
    print(f"             Account Balance: {thisAccount['balance']}")
    print()


def getBalance(accountNumber, accountPassword):
    thisAccount = accountList[accountNumber]
    if accountPassword != thisAccount['password']:
        print("Incorrect Password")
        return None
    else:
        return thisAccount['balance']

# creating 2 accounts
newAccount("Bilal", 100000, 'xxx')
newAccount("Usman", 500, 'yyy')


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
        try:
            account_number = int(input("Please enter your account number:\n"))
        except:
            print("Please enter a valid account")
            print()
            continue
        account_password = input("Please enter your account password:\n")

        balance = getBalance(account_number, account_password)
        if balance is not None:
            print(f"Your Account Balance is: {balance}")
        
    if user_input == 'd':
        print("Deposit functionallity not available for now")
        continue

    if user_input == 'q':
        print("Quitting the game!")
        print()
        break