#Ikbel El Amri
#CodeAcademy unit 11 project
#Classes
#Bank Account

"""This project constitutes a Python class that can be used
to create and manipulate a personal bank account.

The Bank class includes the following methods:
    Accepting deposits
    Allowing withdrawals
    Showing the balance
    Showing the details of the account"""

class BankAccount(object):
    #member variable representing the starting balance of any new BankAccount object
    balance = 0

    def __init__(self, name):
        """initializes instance of the class"""
        self.name = name #specifies who the account belongs to

    def __repr__(self):
        """defines what represents the object when a user tries to print that object using print"""
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)

    def show_balance(self):
        """prints the balance"""
        print "Balance: $%.2f" % (self.balance)

    def deposit(self, amount):
        """deposits amount to the bank account"""
        if amount <= 0: #error checking
            print "Invalid Entry." #error message
            return
        else: #if deposit successful
            print "Amount deposited: $%.2f" % (amount) #print message
            self.balance += amount #increment balance with deposit amount
            self.show_balance() #display the new balance

    def withdraw(self, amount):
        """withdraws from the bank account"""
        #error checking
        if amount > self.balance: #withdrawal amount cannot be greater than current balance
            print "Low funds."
            return
        if amount <= 0 :
            print "Invalid entry."
            return
        else: #if withdrawal successful
            print "Amount withdrew: $%.2f" % (amount) #print message
            self.balance -= amount #dencrement balance with withdrawal amount
            self.show_balance() #display the new balance


my_account = BankAccount("John Doe")
print my_account #print my_account object (through the __repr__ method)
my_account.show_balance() #show balance
my_account.deposit(2000) #deposit $2000
my_account.withdraw(1000) #withdraw $1000
print my_account #test if the __repr__() method accurately reflects these changes 
