"""
Grading System
Author: Harsh Nandal
Description: Assigns grades based on marks obtained.
"""

# Get user input
marks_input = input("Please enter your marks (0-100): ")

# Validate input
if marks_input.isdigit():
    marks = int(marks_input)

    if 0 <= marks <= 100:
        if marks >= 90:
            grade = "A+"
            message = "Excellent!"
        elif marks >= 80:
            grade = "A"
            message = "Very Good!"
        elif marks >= 70:
            grade = "B"
            message = "Above Average"
        elif marks >= 60:
            grade = "C"
            message = "Average"
        elif marks >= 50:
            grade = "D"
            message = "Needs Improvement"
        else:
            grade = "F"
            message = "Fail. Better try again."

        print(f"Your Grade: {grade} | {message}")
    else:
        print("Marks must be between 0 and 100.")
else:
    print("Invalid input. Please enter a numeric value.")
