class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def process_transaction(self, amount):
        self.balance -= amount
        self.transaction_limit += 1

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}, Transaction Limit: {self.transaction_limit}")


# Create objects and test inheritance
Account1 = Account(123456, 5000)
Account1.display_info()

savings = SavingsAccount(123456, 5000, 5)
savings.add_interest()
savings.display_info()

checking = CheckingAccount(123456, 5000, 10)
checking.process_transaction(1000)
checking.display_info()
