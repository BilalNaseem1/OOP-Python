accountName = ''
accountBalance = 0
accountPassword = ''

def createAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
        print('Show:')
        print('            Name', accountName)
        print('            Balance:', accountBalance)
        print('            Password:', accountPassword)
        print()
    

def getBalance(password):
    if password != accountPassword:
        print("Incorrect password")
        return None
    else:
        return accountBalance

def depositAmount(deposit_amount, password):
    global accountBalance
    if password != accountPassword:
        print("Incorrect password")
        return None
    elif deposit_amount <1:
        print("Amount too low to be deposited")
        return None
    else:
        print("Deposit Complete")
        print(f"Amount before deposit {accountBalance}")
        accountBalance += deposit_amount
        print(f"Amount before deposit {accountBalance}")
        return accountBalance

def withdrawAmount(withdraw_amount, password):
    global accountBalance
    if password != accountPassword:
        print("Incorrect password")
        return None
    elif withdraw_amount < 1:
        print("withdraw amount too low")
        return None
    elif withdraw_amount > accountBalance:
        print("withdraw amount cannot be greater than the account balance")
        return None
    else:
        print("Deposit Complete")
        print(f"Amount before deposit {accountBalance}")
        accountBalance -= withdraw_amount
        print(f"Amount before deposit {accountBalance}")
        return accountBalance

createAccount("Joe", 100, 'soup') 
while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')

    print()
    print()
    user_input = input("What do you want to do? \n").lower()
    user_input = user_input[0]

    if user_input not in ('b', 'd', 'w', 's', 'q'):
        print("Please enter a valid input")
        print()
        continue

    if user_input == 'b':
        print('Get Balance')
        user_pswd = input('Please enter your password ')
        the_balance = getBalance(user_pswd)
        if the_balance is not None:
            print("the balance is", the_balance)

    elif user_input == 'd':
        try:
            deposit_amount = float(input("Please enter the amount you want to deposit "))
        except:
            print("Invalid input")
            print()
            continue


        user_pswd = input('Please enter your password ')

        if user_pswd != accountPassword:
            print('Incorrect Password')
        else:
            deposit = depositAmount(deposit_amount, user_pswd)
            if deposit is not None:
                print(f"The deposit amount is {deposit}")
    
    elif user_input == 'w':
        try:
            withdraw_amount = float(input("Please enter the amount you want to withdraw "))
        except:
            print("Invalid Input")

        user_pswd = input('Please enter your password ')
        if user_pswd != accountPassword:
            print('Incorrect Password')
        else:
            withdraw = withdrawAmount(withdraw_amount, user_pswd)
            if withdraw is not None:
                print(f"The withdraw amount is {withdraw}")

    elif user_input == 's':
        show = show()
        if show is not None:
            print(show)

    elif user_input == 'q':
        print('Quitting program')
        break

