
class BankAccount:

    def __init__(self, acc_holder_name, acc_number, balance):

        self.acc_holder_name = acc_holder_name
        self.acc_number = acc_number
        self.balance = balance

    def display_account_info(self):
        print(f"Account holder name : {self.acc_holder_name}, Account number : {self.acc_number}, Balance : {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit of amount {amount} successfull, updated balance : {self.balance}")

    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
            print(f"Withdrawal of {amount} successfull, latest balance : {self.balance}")
        else:
            print("Insufficient account balance")



user1 = BankAccount("Ram", 1, 1000)
user2 = BankAccount("Jai", 2, 5000)
user3 = BankAccount("Rahul",3, 7000)


user1.display_account_info()
user2.display_account_info()
user3.display_account_info()


user2.deposit(10000)
user3.withdraw(4000)
user1.withdraw(10000)


user1.display_account_info()
user2.display_account_info()
user3.display_account_info()
