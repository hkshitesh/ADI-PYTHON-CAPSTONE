class BankAccount:
    def __init__(self, name, acc_num, balance):
        self.account_holder_name = name
        self.account_number = acc_num
        self.balance = balance

    def display_account_info(self):
        print("*" * 80)
        print(f"Account Holder Name : {self.account_holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Balance : {self.balance}")
        print("*" * 80)

    def deposit(self,amount):
        self.balance += amount
        self.display_account_info()
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Can't Withdraw {amount}. Account balance : {self.balance}")
        else:
            self.balance -= amount
            self.display_account_info()


selva = BankAccount("Selva", 12345, 1000)
sagar = BankAccount("Sagar", 12346, 100)
swaroop = BankAccount("Swaroop", 12347, 100)

l = [selva, sagar, swaroop]

for x in l:    
    x.display_account_info()

    x.withdraw(5000)
    x.deposit(10000)
    x.withdraw(5000)
