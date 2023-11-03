class BankAccount:

    def __init__(self, name, account_number, balance):
        self.account_holder_name = name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}")

    def deposit(self, amount):
        self.balance +=amount
        print(f"Amount deposit: {self.balance}")

    def withdraw(self, amount):
        if self.balance <= amount:
            print(f"Insufficient Balance to withdraw, Balance {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn : {self.balance}")


bank_acc1 = BankAccount(name="Somali", account_number=1010, balance=100)
bank_acc2 = BankAccount(name="Kishor", account_number=1100, balance=1000)

bank_acc1.display_account_info()
bank_acc2.display_account_info()

bank_acc1.deposit(100)
bank_acc2.deposit(10)

bank_acc1.withdraw(10)
bank_acc2.withdraw(100)
