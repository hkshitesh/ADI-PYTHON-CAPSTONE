class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    def withdraw(self):
        print(f"Balance after withdrawel: {self.balance}")

    def deposit(self):
        print(f"Balance after deposit: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self):
        print(f"Balance after withdrawel from SB Account: {self.balance}")

    def deposit(self):
        print(f"Balance after deposit from SB Account: {self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self):
        print(f"Balance after withdrawel from CA Account: {self.balance}")

    def deposit(self):
        print(f"Balance after deposit from CA Account: {self.balance}")


bankaccounts = [
    SavingsAccount(12345, 1000),
    CheckingAccount(56789, 2000)
]

for item in bankaccounts:
    print(f"balance after withdraw: {item.withdraw()}\n")
    print(f"balance after deposit: {item.deposit()}\n")