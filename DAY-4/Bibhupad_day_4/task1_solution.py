class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def display_info(self):
        print(f"Name: {self.name}, acc no: {self.number}, balance: {self.balance}")
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,withdraw):
        self.balance -= withdraw

if __name__ =='__main__':
  # Create an object of the class
  person1 = BankAccount("John Doe", 20, 100)
  person2 = BankAccount("Jane Smith", 21, 200)

  # Display the information using the method
  person1.display_info()
  person2.display_info()

  person1.deposit(100)
  person2.withdraw(50)

   # Display the information using the method
  person1.display_info()
  person2.display_info()

