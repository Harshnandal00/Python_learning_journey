# Day 03 Mini Project: Number Analyzer
# Tracks numbers entered by the user and gives count, total, highest, and average

count = 0
total = 0
highest_number = None  # Use None to handle first number dynamically

while True:
    user_input = input("Enter any number (-4 to stop): ")

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue  # Skip invalid inputs

    if number == -4:
        break

    # Update counts and totals
    count += 1
    total += number

    # Update highest number
    if highest_number is None or number > highest_number:
        highest_number = number

# Show final results
if count > 0:
    print("\nSummary of numbers entered:")
    print("Total numbers entered:", count)
    print("Sum of numbers:", total)
    print("Highest number:", highest_number)
    print("Average of numbers:", total / count)
else:
    print("No numbers entered. Please enter some next time!")
