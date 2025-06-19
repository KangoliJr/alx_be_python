class BankAccount:
    def __init__(self,initial_balance=0):
        #starts the bank account at zero
        if not isinstance (initial_balance, (int, float)) or initial_balance <0:
            raise ValueError("Initial must be zero")
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <=0:
            raise ValueError("deposit amount thats greater than zero")
        self.account_balance += amount
        print(f"Deposited: ${amount:2f}")
        
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <=0:
            raise ValueError("Positive number")
        if self.account_balance >= amount:
           self.account_balance -= amount
           print(f"Withdraw: ${amount:.2f}")
           return True
        else:
           print("Insufficient funds")
           return False
       
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
       
    
        
        
        