class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"Name: {self.account_holder_name}, Account Number {self.account_number}, Balance {self.balance}")

    def deposit(self, amount):
        self.balance+=amount
        print(f"Updated balance is {self.balance}")

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Balance\n")
        else:
            self.balance-=amount
            print(f"Updated Balance is {self.balance}")

acc1 = BankAccount("Kiran", 12, 5000)
acc1.display_account_info()
acc1.deposit(5000)
acc1.withdraw(2000)