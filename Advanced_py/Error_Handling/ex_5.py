class MoneyNotEnoughError(Exception):
    pass
class PINCodeError (Exception):
    pass
class UnderageTransactionError (Exception):
    pass
class MoneyIsNegativeError (Exception):
    pass
bank_account = input().split(', ')
PIN_code = int(bank_account[0])
balance = int(bank_account[1])
age = int(bank_account[2])
MIN_AGE = 18
while True:
    command = input().split('#')
    if command[0] == 'Send Money':
        money = int(command[1])
        pin = int(command[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != PIN_code:
            raise PINCodeError("Invalid PIN code")
        if int(age) < MIN_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        print(f"Successfully sent {money:.2f} money to a friend")
        balance -= money
        print(f"There is {balance:.2f} money left in the bank account")

    elif command[0] == 'Receive Money':
        money = int(command[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += money/2
        print(f"{money/2:.2f} money went straight into the bank account")
