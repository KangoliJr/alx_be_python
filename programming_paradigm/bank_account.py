class BankAccount:
    def __init__(self, initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.account_balance += amount
        
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
       
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
        
        
        