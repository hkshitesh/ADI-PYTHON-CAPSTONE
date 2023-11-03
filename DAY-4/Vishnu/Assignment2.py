
class Account:

    def __init__(self, acc_num, balance):
        self.account_number = acc_num
        self.balance = balance

    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}")


class SavingsAccount(Account):
    def __init__(self, acc_num, balance, int_rate):
        super().__init__(acc_num, balance)
        self.int_rate = int_rate

    def add_interest(self, int_rate):
        self.int_rate += int_rate


    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}, Int Rate : {self.int_rate}")

class CheckingAccount(Account):
    def __init__(self, acc_num, balance, transaction_limit):
        super().__init__(acc_num, balance)
        self.transaction_limit = transaction_limit

    def process_transaction(self, amount):
        self.balance -= amount
        self.transaction_limit -= amount

    def display_info(self):
        print(f"Account Number : {self.account_number}, Balance : {self.balance}, Transaction Limit : {self.transaction_limit}")



Acc1 = Account(1, 10000)
SAcc = SavingsAccount(2, 20000, 4)
CAcc = CheckingAccount(3, 30000, 10000)


Acc1.display_info()
SAcc.display_info()
CAcc.display_info()

SAcc.add_interest(1)
CAcc.process_transaction(1000)

SAcc.display_info()
CAcc.display_info()
