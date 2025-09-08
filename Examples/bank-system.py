# -----------------------------
# Bank Account Class Example
# -----------------------------
class Account:
    """
    A simple Bank Account class to manage deposits, withdrawals, and display account details.
    """
    def __init__(self, no, name, bal):
        self.accountNumber = no
        self.accountHolderName = name
        self.balance = bal

    # Getters and Setters
    def getName(self):
        return self.accountHolderName

    def setName(self, name):
        self.accountHolderName = name

    def getAccNo(self):
        return self.accountNumber

    def setAccNo(self, no):
        self.accountNumber = no

    def getBal(self):
        return self.balance

    def setBal(self, bal):
        self.balance = bal

    # Display account details
    def details(self):
        print(f"Account Number: {self.accountNumber}, Name: {self.accountHolderName}, Balance: {self.balance}")

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"\nAfter deposit of {amount}, new balance: {self.balance}")

    # Withdraw money
    def withdraw(self, amount):
        if self.balance < amount or self.balance == 0:
            print("\nInsufficient balance")
        else:
            self.balance -= amount
            print(f"\nAfter withdrawal of {amount}, new balance: {self.balance}")


# -----------------------------
# Create account objects
# -----------------------------
a1 = Account(1, "Alice", 1100)
a2 = Account(2, "Bob", 1200)
a3 = Account(3, "Charlie", 1300)
a4 = Account(4, "David", 1400)
a5 = Account(5, "Eve", 1500)

# Store accounts in a list
accounts = [a1, a2, a3, a4, a5]

# Display all account details
print("All account details:")
for acc in accounts:
    acc.details()

# Deposit example
a2.deposit(500)
a2.details()

# Withdraw example
a5.withdraw(1000)
a5.details()
