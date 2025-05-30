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
    if accountPassword == thisAccount['password']:

