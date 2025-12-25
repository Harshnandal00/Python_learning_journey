count = 0
total_expense = 0
highest_expenditure = 0

while True:
    user_input = (input("enter your expenses here(To exit press q): ")).lower()

    if user_input == ("q"):
        break

    try:
        expense = float(user_input)
    except ValueError:
        print("Invalid Input! please enter a number.")

    count += 1
    total_expense += expense
    
    if highest_expenditure < expense:
        highest_expenditure = expense

if count > 0:
    print("No. of expenses entered: ",count)
    print("Total expenditure: ", total_expense)
    print("Highest purchase/expenditure by user: ", highest_expenditure)
else:
    print("Please enter some expenses first!")