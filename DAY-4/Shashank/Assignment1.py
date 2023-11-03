class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def display_account_info(self):
        print(f"Name: {self.name}, Account Number: {self.acc_no}, Major: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Amount : {amount} New Balance : {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"withdraw Amount : {amount} New Balance : {self.balance}")


Account1 = BankAccount('Chetan', 123456, 5000)
Account1.display_account_info()
Account1.deposit(1000)
Account1.withdraw(2000)
Account1.display_account_info()