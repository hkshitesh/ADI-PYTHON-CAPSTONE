class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def process_transaction(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited : {amount} , New Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount Withdrawed : {amount} , New Balance: {self.balance}")

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    def process_transaction(self, amount):
        pass


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def process_transaction(self, amount):
        self.balance -= amount
        self.transaction_limit += 1

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}, Transaction Limit: {self.transaction_limit}")


Accounts = [
    Account(245678, 10000),
    SavingsAccount(123456, 5000),
    CheckingAccount(246787, 7000, 10)
]

for items in Accounts:
    items.display_info()
    items.withdraw(1000)
    items.deposit(1000)
    items.process_transaction(1000)
    