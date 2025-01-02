# Welcome to WIT International Bank!


def main() -> None:
    """Define Users accounts
    Here we have a list of users, each with a card number, pin, and balance (money they have)
    """
    accounts = {
        "1000717569": {"pin": "182963", "balance": 22000},
        "1000712483": {"pin": "248695", "balance": 50000},
        "1000714218": {"pin": "794587", "balance": 48233},
        "1000712487": {"pin": "332475", "balance": 10000},
        "1000715562": {"pin": "647812", "balance": 500},
        "1000713377": {"pin": "220154", "balance": 3},
    }

    # Try to log in the user
    # Ask for the card number and PIN to check if it's correct
    user = authenticate_user(accounts)
    if not user:
        print("Authentication failed. Exiting program.")
        return
# Define Users accounts Here we have a list of users, each with a card number, pin,
# and balance (money they have)
    while True:
        choice = display_menu()
        if choice == "1":
            check_balance(accounts, user)
        elif choice == "2":
            deposit_cash(accounts, user)
        elif choice == "3":
            withdraw_cash(accounts, user)
        elif choice == "4":
            print(
        "Thank you for choosing WIT International Bank. The Bank that you can always rely on."
            )
            break  # End the program when user chooses to exit
        else:
            print("Invalid choice! Please select a valid option.")


# Function to check if the user is logging in with the right card number and PIN
def authenticate_user(accounts):
    """
    Function to check if the user’s card number and PIN are correct.
    If they are, we return the card number, otherwise, we return None.
    """
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    # If the card number exists and the PIN matches, log the user in
    if card_number in accounts and accounts[card_number]["pin"] == pin:
        print("Authentication successful!")
        return card_number
    # If something is wrong with the login, show an error message
    print("Invalid credentials!")
    return None


# Function to show the menu with choices like check balance, deposit, withdraw, or exit
def display_menu():
    """
    Shows the choices the user can pick and returns the one they choose.
    """
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Cash")
    print("3. Withdraw Cash")
    print("4. Exit")

    # Keep asking until the user picks a correct option
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


# Function to show the user how much money they have in their account
def check_balance(accounts, user):
    """
    Shows the user their balance (how much money is in their account).
    """
    print(f"Your balance is: ${accounts[user]['balance']}")


# Function to add money to the user's account
def deposit_cash(accounts, user):
    """
    Lets the user add money to their account.
    It makes sure the amount they enter is positive.
    """
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                accounts[user]["balance"] += amount
                print(
                    f"${amount} deposited successfully. New balance: ${accounts[user]['balance']}"
                )
                break
            else:
                print("Invalid deposit amount! Please enter a positive value.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to let the user take money out of their account
def withdraw_cash(accounts, user):
    """
    Lets the user take money out of their account.
    It makes sure they have enough money and that they enter a positive number.
    """
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= accounts[user]["balance"]:
                accounts[user]["balance"] -= amount
                print(
                    f"${amount} withdrawn successfully. New balance: ${accounts[user]['balance']}"
                )
                break
            else:
                print(
                    "Insufficient balance or invalid amount! Please check and try again."
                )
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# This starts the program
if __name__ == "__main__":
    main()
