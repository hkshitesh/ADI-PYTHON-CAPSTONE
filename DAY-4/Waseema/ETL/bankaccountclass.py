class BankAccount:
    def __init__(self,acc_name,acc_num,bal):
        self.acc_name = acc_name
        self.acc_num = acc_num
        self.bal = bal

    def deposit(self,amount):
        self.bal = self.bal + amount


    def withdraw(self,amount):
        if amount > self.bal:
            print(f"Insufficient balance in {self.acc_name}'s account")
            raise ValueError
        else:
            self.bal = self.bal - amount

    def display(self):
        print(f"Name:{self.acc_name}, Account Number: {self.acc_num}, Balance:{self.bal}")
#User 1
Acc1 = BankAccount("John",12345,15000)
Acc1.display()

Acc1.deposit(6000)
Acc1.display()
Acc1.withdraw(7000)
Acc1.display()



#User2
Acc2 = BankAccount("Kavitha",54678,10000)
Acc2.display()

Acc2.deposit(6000)
Acc2.display()

#For insufficent balance
Acc1.withdraw(17000)
Acc1.display()