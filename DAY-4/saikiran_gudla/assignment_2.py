class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number {self.account_number}, Balance {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance*=(1+self.interest_rate/100.0)

    def display_info(self):
        print(f"Account Number {self.account_number}, Balance {self.balance}, Interest {self.interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def process_transaction(self, amount):
        self.transaction_limit-=amount

    def display_info(self):
        print(f"Account Number {self.account_number}, Balance {self.balance}, Transaction Limit {self.transaction_limit}")


if __name__ == '__main__':
    acc1 = SavingsAccount(1, 1000, 5)
    acc2 = CheckingAccount(2, 2000, 500)

    acc1.display_info()
    acc2.display_info()

    acc1.add_interest()
    acc1.display_info()

    acc2.process_transaction(200)
    acc2.display_info()