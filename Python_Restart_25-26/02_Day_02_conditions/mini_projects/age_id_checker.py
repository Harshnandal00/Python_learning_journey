"""
Age and ID Checker
Author: Harsh Nandal
Description: Checks if a user is of age and has a valid ID.
"""

# Get user input
age_input = input("Enter your age: ")

# Validate numeric input
if age_input.isdigit():
    age = int(age_input)
    has_id = input("Do you have an ID? (yes/no): ").strip().lower()

    if age >= 18:
        if has_id == "yes":
            print("Access authorized. Welcome!")
        elif has_id == "no":
            make_id = input("Do you want to register and create an ID? (yes/no): ").strip().lower()
            if make_id == "yes":
                print("Registration successful. Access granted!")
            else:
                print("Access denied. ID is required.")
        else:
            print("Invalid input for ID. Please enter 'yes' or 'no'.")
    else:
        print("Access denied. You are underage.")
else:
    print("Invalid age entered. Please enter a number.")
