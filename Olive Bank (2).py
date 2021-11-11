import random as rd

class DataBank:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account_no = rd.randrange(0000000000, 9999999999)
        self.account_bal = 0        

    def get_name(self):
        return self.name

    def check_balance(self):
        return f"Your account balance is: {self.account_bal}"

    def deposit(self, value):
        self.account_bal += value
        print("Transaction Sucessful!")

    def withdrawal(self, value):
        if self.account_bal >= value:
            self.account_bal -= value
            print("Transaction Successful!")
        else:
            print("Insufficient Funds!")


print("Welcome to Olive Bank\n")
ask_name = input("Enter name here: ")
ask_age = input("Enter age here: ")

customer = DataBank(ask_name, ask_age)
print(f"Welcome {customer.get_name()}")
def menu():
    while True:
        print("\n")
        print("Enter 1 to access acount balance\nEnter 2 to make deposits\nEnter 3 to make withdrawal\nEnter 9 to quit")
        ask = int(input("Enter option here: "))
        if ask == 1:
            print(customer.check_balance())
        elif ask == 2:
            further = int(input("Enter amount here: "))
            customer.deposit(further)
        elif ask == 3:
            further = int(input("Enter amount here: "))
            customer.withdrawal(further)
        elif ask == 9:
            print("Thank you for banking with us!")
            break

menu()