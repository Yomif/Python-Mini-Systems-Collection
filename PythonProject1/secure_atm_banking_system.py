# ==========================================
#        SECURE ATM BANKING SYSTEM
# ==========================================

# Initial account balance
balance = 50000

print("===================================")
print("     WELCOME TO PYTHON BANK")
print("===================================")

# User PIN authentication
try:
    pin = int(input("Enter your 4-digit PIN: "))

    if pin == 1234:

        print("\nAccess Granted")
        print("===================================")

        # Display ATM menu
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # User chooses an option
        choice = int(input("\nChoose an option: "))

        # Option 1 - Check Balance
        if choice == 1:
            print(f"\nYour current balance is: ₦{balance:,.2f}")

        # Option 2 - Deposit
        elif choice == 2:

            deposit = float(input("Enter amount to deposit: ₦"))

            if deposit > 0:
                balance += deposit

                print("\nDeposit Successful")
                print(f"Updated Balance: ₦{balance:,.2f}")

            else:
                print("Deposit amount must be greater than zero.")

        # Option 3 - Withdraw
        elif choice == 3:

            withdraw = float(input("Enter amount to withdraw: ₦"))

            if withdraw <= 0:
                print("Withdrawal amount must be greater than zero.")

            elif withdraw <= balance:
                balance -= withdraw

                print("\nWithdrawal Successful")
                print(f"Remaining Balance: ₦{balance:,.2f}")

            else:
                print("Insufficient Funds.")

        # Option 4 - Exit
        elif choice == 4:
            print("Thank you for using Python Bank ATM.")

        # Invalid option
        else:
            print("Invalid menu option selected.")

    else:
        print("Incorrect PIN. Access Denied.")

# Handle invalid input
except ValueError:
    print("Invalid input. Please enter numbers only.")

print("===================================")
print("        SESSION TERMINATED")
print("===================================")