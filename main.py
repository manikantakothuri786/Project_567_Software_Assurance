class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def change_holder_name(self, new_name):
        self.account_holder = new_name

    def close_account(self):
        self.balance = 0
        self.account_holder = "Closed Account"

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
