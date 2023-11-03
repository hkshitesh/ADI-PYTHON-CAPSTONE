class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += (self.balance*self.interest_rate)

    def withdraw(self, amount):
        print(f"New balance with Interest:{self.balance}")
        self.add_interest()
        self.balance -= amount
        print(f"Amount:{amount} Withdrawn")

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance with Interest:{self.balance}")
        print(f"Amount:{amount} deposited")
        self.add_interest()

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def check_transaction_limit(self, amount):
        if self.transaction_limit <= amount:
            print(f"Transaction Limit: {self.transaction_limit}, Amount:{amount} can not be withdrawn")
            return "Not enough Balance"
        else:
            return "Enough Transaction Limit"

    def withdraw(self, amount):
        ret_str = self.check_transaction_limit(amount)
        if ret_str == "Enough Transaction Limit":
            self.balance -= amount
            print(f"Amount:{amount} Withdrawn")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount:{amount} deposited")

    def display_info(self):
        super().display_info()
        print(f"Transaction Limit: {self.transaction_limit}")


# Create objects and test inheritance
print("\nACCOUNT1 TESTS")
acc1 = SavingsAccount(12345,10000,0.02)
acc1.withdraw(1000)
acc1.deposit(2000)
acc1.display_info()

print("\nACCOUNT2 TESTS")
acc2 = CheckingAccount(123456,1000,1000)
acc2.withdraw(2000)
acc2.deposit(3000)
acc2.display_info()

