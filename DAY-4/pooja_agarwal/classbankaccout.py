class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print(f"Account Holder Name: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
        else:
            print("\n Low Balance")

# Create an object of the class
holder1 = BankAccount("Dino James", 20568, 15000)
holder2 = BankAccount("Arijeet Shetty", 21658, 10000)

# Display the information using the method
holder1.display_account_info()
holder2.display_account_info()

#Deposit amount
holder1.deposit(5000)
holder2.deposit(3000)

# Display the information using the method
holder1.display_account_info()
holder2.display_account_info()

#Deposit amount
holder1.withdraw(3000)
holder2.withdraw(5000)

# Display the information using the method
holder1.display_account_info()
holder2.display_account_info()

#Deposit amount
holder1.withdraw(30000)
holder2.withdraw(59000)