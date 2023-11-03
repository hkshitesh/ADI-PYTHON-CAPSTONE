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
        interest_amt = self.balance * (self.interest_rate / 100)
        self.balance += interest_amt

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def process_transaction(self, withdraw_amt):
        if self.transaction_limit > 0:
            if withdraw_amt <= self.balance:
                self.balance -= withdraw_amt
                self.transaction_limit -= 1
                print(f"Transaction of ${withdraw_amt:.2f} processed.")
            else:
                print("Insufficient funds for this transaction.")
        else:
            print("Transaction limit reached for this account.")

    def display_info(self):
        super().display_info()
        print(f"Transaction Limit: {self.balance}")


sa1 = SavingsAccount("101", 1000.0, 2.5)  # Savings account with a 2.5% interest rate
sa2 = SavingsAccount("102", 10000.0, 4.5)  # Savings account with a 4.5% interest rate
sa3 = SavingsAccount("103", 100000.0, 6.5)  # savings account with a 6.5% interest rate

ca1 = CheckingAccount("110",1000, 5)  # Savings account with a 2.5% interest rate
ca2 = CheckingAccount("111", 10000.0, 10)  # Savings account with a 4.5% interest rate
ca3 = CheckingAccount("112", 100000.0, 10)  # savings account with a 6.5% interest rate

print("\n\rDisplay Savings Account with Initial Balance Information \n")
sa1.display_info()  # Display account information
sa2.display_info()  # Display account information
sa3.display_info()  # Display account information

print("\n\rAdding Interest to Saving Accounts \n")
sa1.add_interest()  # Add interest
sa2.add_interest()  # Add interest
sa3.add_interest()  # Add interest

sa1.display_info()  # Display account information
sa2.display_info()  # Display account information
sa3.display_info()  # Display account information

print("\n\rTrying to withdraw \n")
ca1.process_transaction(250)  # Add interest
ca2.process_transaction(4500)  # Add interest
ca3.process_transaction(65000)  # Add interest

ca1.display_info()  # Display account information
ca2.display_info()  # Display account information
ca3.display_info()  # Display account information