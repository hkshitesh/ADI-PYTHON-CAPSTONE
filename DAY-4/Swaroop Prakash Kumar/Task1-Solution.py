class BankAccount:

    def __init__(self, name, account_number, balance):
        self.account_holder_name = name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"Account Holder's Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")
        return

    def deposit(self, amount):
        self.balance += amount
        return

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not Enough Money. Work Harder!!")
        else:
           self.balance -= amount
        return


account1 = BankAccount("Swaroop1", 1, 10)
account2 = BankAccount("Swaroop2", 2, 100)
account3 = BankAccount("Swaroop3", 3, 1000)

print("Before Withdraw!!")
account1.display_account_info()
account2.display_account_info()
account3.display_account_info()

account1.withdraw(50)
account2.withdraw(50)
account3.withdraw(50)

print("After Withdraw!!")
account1.display_account_info()
account2.display_account_info()
account3.display_account_info()

print("After Deposit!!")
account1.deposit(500)
account2.deposit(500)
account3.deposit(500)