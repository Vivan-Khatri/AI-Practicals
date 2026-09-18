# Simple Banking System Simulator

def show_menu():
    print("\n--- Welcome to Python Bank ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("------------------------------")

def check_balance(balance):
    # Displays the current balance to the user
    print(f"\nYour current account balance is:  Rs {balance}")

def deposit(balance):
    # Handles adding money to the account
    amount = float(input("Enter amount to deposit:  Rs "))
    if amount > 0:
        balance = balance + amount
        print(f"\nSuccess! You have deposited  Rs {amount}.")
    else:
        print("\nError: Please enter a positive number.")
    return balance

def withdraw(balance):
    # Handles taking money out with a safety check
    amount = float(input("Enter amount to withdraw:  Rs "))
    if amount > 0:
        if amount <= balance:
            balance = balance - amount
            print(f"\nSuccess! You have withdrawn  Rs {amount}.")
        else:
            print("\nError: Insufficient funds in your account!")
    else:
        print("\nError: Please enter a positive number.")
    return balance

def main():
    # Main system loop and starting balance
    current_balance = 0.0
    system_running = True

    while system_running:
        show_menu()
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            check_balance(current_balance)
        elif choice == '2':
            current_balance = deposit(current_balance)
        elif choice == '3':
            current_balance = withdraw(current_balance)
        elif choice == '4':
            print("\nThank you for using Python Bank. Have a great day!\n")
            system_running = False
        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")

# Starts the program
if __name__ == "__main__":
    main()