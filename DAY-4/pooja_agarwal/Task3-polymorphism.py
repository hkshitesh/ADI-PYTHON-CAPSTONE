class Account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")
        return

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass


class SavingsAccount(Account):

    def __init__(self, account_number, balance, interest):
        self.interest_rate = interest
        super().__init__(account_number, balance)

    def add_interest(self):
        self.deposit(self.balance * self.interest_rate/100)
        return

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}")
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


class CheckingAccount(Account):

    def __init__(self, account_number, balance, transaction_limit):
        self.transaction_limit = transaction_limit
        super().__init__(account_number, balance)

    def process_transaction(self, amount):
        if not self.transaction_limit:
            print("Transaction Limit Reached")
            return
        self.transaction_limit -= 1
        self.withdraw(amount)
        return

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")
        print(f"Transaction Limit: {self.transaction_limit}")
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


s = SavingsAccount(1, 200, 300)
print("Before Interest")
s.display_info()
s.add_interest()
print("After Interest")
s.display_info()


s = CheckingAccount(2, 300, 3)
s.display_info()
s.process_transaction(10)
s.process_transaction(10)
