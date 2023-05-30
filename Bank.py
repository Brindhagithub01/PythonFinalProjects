import pwinput
import random
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                return customer
        return None


class Customer:
    def __init__(self, name, account_number,pin):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.pin=pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >1:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

def create_customer():
        name = input("Enter customer name: ")
        account_number = int(input("Enter the account number"))
        pin = int(pwinput.pwinput("Enter four digit PIN:", mask='*'))
        print("\n\tCustomer Name:", name, "\n\tAccount Number", account_number, "\n\tPin No", pin)
        return Customer(name, account_number, pin)

def display_menu():
        print("\t\tHello!!! Welcome to Bank Management System\t\t")
        print("1. Create a new customer")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Check account balance")
        print("5. Exit")


bank = Bank("MyBank")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        customer = create_customer()
        bank.add_customer(customer)
        print("Customer created successfully.")

    elif choice == "2":
        account_number = int(input("Enter account number: "))
        pin = int(pwinput.pwinput("Enter four digit PIN:", mask='*'))
        customer = bank.get_customer(pin) and bank.get_customer(account_number)
        if customer:
            amount = float(input("Enter deposit amount: "))
            customer.deposit(amount)
        else:
            print("Customer not found.")

    elif choice == "3":
        account_number = int(input("Enter account number: "))
        pin = int(pwinput.pwinput("Enter four digit PIN:", mask='*'))
        customer = bank.get_customer(pin) and bank.get_customer(account_number)
        if customer:
            amount = float(input("Enter withdrawal amount: "))
            customer.withdraw(amount)
        else:
            print("Customer not found.")

    elif choice == "4":
        account_number = int(input("Enter account number: "))
        pin = int(pwinput.pwinput("Enter four digit PIN:", mask='*'))
        customer = bank.get_customer(pin) and bank.get_customer(account_number)
        if customer:
            balance = customer.get_balance()
            print(f"Account balance: {balance}")
        else:
            print("Customer not found.")

    elif choice == "5":
        print("Exiting Bank Management System...")
        break

    else:
        print("Invalid choice. Please try again.")
