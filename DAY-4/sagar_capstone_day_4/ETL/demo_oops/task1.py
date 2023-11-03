class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f'Name:{self.account_holder_name}, AccountNumber:{self.account_holder_name}, Balance:{self.balance}')

    def deposit(self, deposit_money):
        self.balance = self.balance + deposit_money

    def withdraw(self, withdrawal_money):
        self.balance = self.balance - withdrawal_money


account_holder1 = BankAccount("Pooja", 1, 100000)
account_holder2 = BankAccount("Selva", 2, 100003)

account_holder1.display_account_info()
account_holder2.display_account_info()

account_holder2.deposit(5)

account_holder2.display_account_info()

