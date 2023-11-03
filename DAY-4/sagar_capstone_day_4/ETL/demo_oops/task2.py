class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f'AccountNumber:{self.account_number}, Balance:{self.balance}')

class Savings(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate) / 100;

    def display_info(self):
        print(f'AccountNumber:{self.account_number}, Balance:{self.balance}, InterestRate:{self.interest_rate}')


account_holder1 = Savings(1, 1000, 10)
account_holder2 = Savings(2, 2000, 5)

account_holder1.add_interest()
account_holder2.add_interest()

account_holder1.display_info()
account_holder2.display_info()


class CheckingAccount(Account):
    def __init__(self, account_number, balance, maximum_transactions):
        super().__init__(account_number, balance)
        self.maximum_transactions = maximum_transactions

    def process_transaction(self):
        self.maximum_transactions = self.maximum_transactions - 1;

    def display_info(self):
        print(f'AccountNumber:{self.account_number}, Balance:{self.balance}, MaximumTransactions:{self.maximum_transactions}')


account_holder3 = CheckingAccount(1, 1000, 10)
account_holder4 = CheckingAccount(2, 2000, 5)

account_holder3.process_transaction()
account_holder4.process_transaction()

account_holder3.display_info()
account_holder4.display_info()