
class Account:

    def __init__(self, acc_num, balance):
        self.account_number = acc_num
        self.balance = balance

    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}")

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, acc_num, balance, int_rate):
        super().__init__(acc_num, balance)
        self.int_rate = int_rate

    def deposit(self,amount):
        self.balance += amount
        print("Deposit to Savings account")

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdraw from Checking account")

    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}, Int Rate : {self.int_rate}")

class CheckingAccount(Account):
    def __init__(self, acc_num, balance, transaction_limit):
        super().__init__(acc_num, balance)
        self.transaction_limit = transaction_limit

    def deposit(self, amount):
        self.balance += amount
        print("Deposit to Checking account")

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdraw from Checking account")
    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}, Transaction Limit : {self.transaction_limit}")



list_accounts = [Account(1, 10000), SavingsAccount(2, 20000, 4), CheckingAccount(3, 30000, 10000)
 ]

for acc in list_accounts:
    acc.display_info()

for acc in list_accounts:
    acc.deposit(1000)
    acc.display_info()


for acc in list_accounts:
    acc.withdraw(1000)
    acc.display_info()
