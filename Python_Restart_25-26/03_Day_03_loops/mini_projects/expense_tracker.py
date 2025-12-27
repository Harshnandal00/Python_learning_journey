# Day 03 Mini Project: Expense Tracker
# Tracks user's expenses and shows total, count, and highest expense

count = 0
total_expense = 0
highest_expenditure = 0

while True:
    user_input = input("Enter your expense (or 'q' to quit): ").lower()

    if user_input == "q":
        break

    try:
        expense = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue  # Skip counting invalid input

    # Update counts and totals
    count += 1
    total_expense += expense

    # Update highest expense
    if expense > highest_expenditure:
        highest_expenditure = expense

# Show results
if count > 0:
    print("\nSummary of your expenses:")
    print("Number of expenses entered:", count)
    print("Total expenditure:", total_expense)
    print("Highest expense:", highest_expenditure)
else:
    print("No expenses entered. Please add some expenses next time!")
