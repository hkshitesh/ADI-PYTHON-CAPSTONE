class Account:
    def __init__(self, acc_num, balance):
        self.account_number = acc_num
        self.balance = balance

    def display_account_info(self):
        print(f"Account Number : {self.account_number}")
        print(f"Account Balance : {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        # self.display_account_info()
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Can't Withdraw {amount}. Account balance : {self.balance}")
        else:
            self.balance -= amount
            # self.display_account_info()


class SavingsAccount(Account):
    def __init__(self, acc_num, balance, int_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = int_rate
    
    def add_interest(self):
        self.deposit(self.balance * (self.interest_rate/100))

    def display_account_info(self):
        super().display_account_info()
        print(f"Interest Rate : {self.interest_rate}")



class CheckingAccount(Account):
    def __init__(self, acc_num, balance, trans_limit):
        super().__init__(acc_num, balance)
        self.transaction_limit = trans_limit
    
    def process_transaction(self,amount):
        if self.transaction_limit:
            self.withdraw(amount)
            self.transaction_limit -= 1
        else:
            print("Exceeded transaction limit")
    
    def display_account_info(self):
        super().display_account_info()
        print(f"Transaction limit : {self.transaction_limit}")



if __name__ == "__main__":
    s = SavingsAccount(12345, 100, 10)
    c = CheckingAccount(456, 50, 2)

    s.display_account_info()
    s.add_interest()
    s.display_account_info()

    c.display_account_info()
    c.process_transaction(10)
    c.display_account_info()
    c.process_transaction(10)
    c.process_transaction(10)
    c.display_account_info()
