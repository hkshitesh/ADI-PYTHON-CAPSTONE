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


class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance, interest_rate):
        super().__init__(account_holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance+=amount
        print(f"You are depositing in savings account")

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Balance\n")
        else:
            self.balance-=amount
            print(f"You are withdrawing from savings account")



class CheckingAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, balance, transaction_limit):
        super().__init__(account_holder_name, account_number, balance)
        self.transaction_limit = transaction_limit

    def deposit(self, amount):
        self.balance+=amount
        print(f"You are depositing in checking account")

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Balance\n")
        else:
            self.balance-=amount
            print(f"You are withdrawing from checking account")

if __name__ == '__main__':
    account_items = [SavingsAccount("Sai", 1, 1000, 5),
                     CheckingAccount("kiran", 2, 2000, 500)]

    for item in account_items:
        item.display_account_info()
        item.deposit(500)
        item.withdraw(200)
        item.display_account_info()
