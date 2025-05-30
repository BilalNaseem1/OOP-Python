accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {
        'name': aName,
        'balamce': aBalance,
        'password': aPassword
    }
    accountList.append(newAccountDict)

def show(accountNumber):
    