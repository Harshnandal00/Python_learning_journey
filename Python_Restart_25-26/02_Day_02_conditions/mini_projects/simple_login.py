"""
Simple Login System
Author: Harsh Nandal
Description: Validates a username and numeric password.
"""

# User input
username = input("Enter username: ").strip().lower()
password_input = input("Enter password (numbers only): ").strip()

# Validate numeric password
if password_input.isdigit():
    password = int(password_input)

    # Check credentials
    if username == "admin" and password == 1245:
        print("Access allowed! Welcome back, admin.")
    else:
        print("Access denied. Username or password is incorrect.")
else:
    print("Password must be numeric. Please try again.")
