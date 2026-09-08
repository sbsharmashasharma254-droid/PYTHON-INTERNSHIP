# Assignment 1: ATM Simulation
# Create a simple ATM program using Python.
# 1. Create a function atm().
# 2. Start with a balance of Rs. 10,000.
# 3. Display a menu: Check Balance, Deposit, Withdraw, Exit.
# 4. Use a loop so the menu keeps appearing until Exit.
# 5. Use conditional statements for selected operations.
# 6. Use assignment operators for deposit and withdrawal.
# 7. Do not allow withdrawal greater than available balance.
# 8. Display updated balance after every transaction.


def atm():
    balance = 10000

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance =", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Updated Balance =", balance)

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Updated Balance =", balance)
            else:
                print("Insufficient Balance")

        elif choice == 4:
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice")


atm()