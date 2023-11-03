class Account:
    def __init__(self,acc_num,bal):
        self.acc_num = acc_num
        self.bal = bal

    def display_info(self):
        print(f"Account No: {self.acc_num}, Balance: Rs.{self.bal}")


class SavingsAccount(Account):
    def __init__(self,acc_num,bal,interest):
        super().__init__(acc_num,bal)
        self.interest = interest

    def add_interest(self):
        self.bal = self.bal - ((self.bal*self.interest)/100)

    def display_info(self):
        print(f"Account No: {self.acc_num}, Balance:Rs. {self.bal}, Interest Rate: {self.interest}")

class CheckingAccount(Account):
    def __init__(self,acc_num,bal):
        super().__init__(acc_num,bal)
        self.limit_num = 0

    def process_transaction(self,amount):
        if amount > self.bal:
            print(f"Insufficient balance in '{self.acc_num}' account")
            raise ValueError
        else:
            if self.limit_num >= 2:
                print(f"Transaction limit exceeded in '{self.acc_num}' Account")
                raise ValueError
            else:
                self.bal = self.bal - amount
                self.limit_num = self.limit_num + 1

    def display_info(self):
        print(f"Account No: {self.acc_num}, Balance:Rs. {self.bal}, Limit: {self.limit_num}%")


acc1 = Account(1234,15000)
acc1.display_info()

savings = SavingsAccount(1345, 54000, 2.5)
savings.add_interest()
savings.add_interest()
savings.display_info()

#transaction limit is 2 times
check = CheckingAccount(7654, 19000)
check.process_transaction(7000)
check.process_transaction(3000)
check.process_transaction(2000)
check.display_info()
