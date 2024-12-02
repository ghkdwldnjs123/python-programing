class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")


account = BankAccount("김대열", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
account.display_balance()
