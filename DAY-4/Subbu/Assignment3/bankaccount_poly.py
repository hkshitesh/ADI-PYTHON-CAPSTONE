class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"AccountNumber: {self.account_number}, Balance: {self.balance}")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
        else:
            print("Insufficient funds")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.transaction_limit:
            self.balance -= amount
        else:
            print("Transaction exceeds overdraft limit")

    def display_account_info(self):
        super().display_account_info()
        print(f"Overdraft Limit: ${self.transaction_limit:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_earned = self.balance * (self.interest_rate / 100)
        self.balance += interest_earned

    def display_info(self):
        super().display_account_info()
        print(f"Interest Rate: {self.interest_rate}%")

# Example usage:
if __name__ == '__main__':
    account1 = CheckingAccount("123456", 10000, 200.0)
    account2 = SavingsAccount("789012", 1500, 2.5)

    account1.display_account_info()
    account1.withdraw(800.0)
    account1.display_account_info()

    account2.display_account_info()
    account2.deposit(1000.0)
    account2.display_account_info()
    account2.add_interest()
    account2.display_account_info()