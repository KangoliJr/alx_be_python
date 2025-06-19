import sys
from bank_account import BankAccount

def main():
    # Initialize BankAccount with an example starting balance
    # You can change this for different testing scenarios
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    
    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Error: Amount must be a number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            account.withdraw(amount)
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        if amount is not None: # Check if an unexpected amount was provided for display
            print("Warning: 'display' command does not take an amount. Ignoring provided amount.")
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()