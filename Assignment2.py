# Assignment 2: Password & Login System
# Create a simple login system using Python.
# Maximum 3 attempts are allowed.
# Check username and password using conditional statements.
# Display "Login successful!" for correct details.
# Display "Account locked!" after 3 incorrect attempts.


def login():
    username = "admin"
    password = "python123"
    attempts = 0

    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == username and pwd == password:
            print("Login successful!")
            break
        else:
            attempts += 1
            print("Incorrect username or password.")

            if attempts < 3:
                print("Attempts remaining:", 3 - attempts)

    if attempts == 3:
        print("Account locked!")


login()