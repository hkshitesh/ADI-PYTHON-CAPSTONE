class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"Name: {self.account_holder_name}, AccountNumber: {self.account_number}, Balance: {self.balance}")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount


#Example Use

# Create an object of the class
customer1 = BankAccount("John Doe", 20, 100000)
customer2 = BankAccount("Jane Smith", 21, 1500000)

# Display the Account information Initially using the method
customer1.display_account_info()
customer2.display_account_info()

# Deposit 100000 Rupees
customer1.deposit(100000)
customer2.deposit(100000)

# Display the Account information after deposit
customer1.display_account_info()
customer2.display_account_info()

# Withdraw 19000 Rupees
customer1.withdraw(19000)
customer2.withdraw(19000)

# Display the Account information after Withdrawl
customer1.display_account_info()
customer2.display_account_info()