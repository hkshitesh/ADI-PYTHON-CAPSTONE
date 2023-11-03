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
        self.balance += (self.balance*self.interest_rate)
        print(f"Current Balance: {self.balance}")

    def display_info(self):
        self.add_interest()
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def process_transaction(self, amount):
        if self.balance<= amount:
            print(f"Not Enough Balance:{self.balance}")
        else:
            self.balance -= amount
            self.transaction_limit -= amount
            print(f"Current Transaction Limit:{self.transaction_limit}")

    def display_info(self):
        super().display_info()
        print(f"Transaction Limit: {self.transaction_limit}")


# Create objects and test inheritance
acc1 = SavingsAccount(12345,10000,0.02)
acc1.display_info()

acc2 = CheckingAccount(123456,1000,1000)
acc2.process_transaction(100)
acc2.display_info()

